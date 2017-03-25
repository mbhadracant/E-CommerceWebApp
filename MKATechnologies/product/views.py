import csv
import json
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from .models import Category
from .models import Subcategory
from .models import Order
from accounts.models import User
from .serializers import  ProductSerializer, SubcategorySerializer
from .serializers import  OrderSerializer
from rest_framework.response import Response
from django.http import Http404, HttpResponse, HttpResponseRedirect
import os

def get_products(request):
        allProducts = Product.objects.all()
        if request.GET.get('category') is not None:
            allProducts = allProducts.filter(product_category__contains=request.GET.get('category'))
        if request.GET.get('brand') is not None:
            allProducts = allProducts.filter(product_make__contains=request.GET.get('brand'))
        if request.GET.get('subcategory') is not None:
            allProducts = allProducts.filter(product_subcategory__contains=request.GET.get('subcategory'))
        if request.GET.get('productName') is not None:
            allProducts = allProducts.filter(product_name__contains=request.GET.get('productName'))
        serializer = ProductSerializer(allProducts, many=True)
        return HttpResponse(json.dumps(serializer.data))

#Gets all the products
class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

#Get product details given a product id
class ProductDetails(APIView):
    def get(self, request):
        product = Product.objects.get(product_id=request.GET.get(''))
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

#Get products given the category
class ProductCategory(APIView):
    def get(self, request):
        products = Product.objects.filter(product_category=request.GET.get(''))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

#Get all the products given the brand
class ProductBrand(APIView):
    def get(self, request):
        products = Product.objects.filter(product_make=request.GET.get(''))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class OrderDetails(APIView):
    def get(self, request):
        order = Order.objects.get(order_id=request.GET.get(''))
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)

class UserOrderDetails(APIView):
    def get(self, request):
        orders = Order.objects.filter(user_id=request.GET.get(''))
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

# #Get user details given user id
# class UserDetails(APIView):
#     def get(self, request):
#         user = Users.objects.get(username=request.GET.get(''))
#         serializer = UserSerializer(user, many=False)
#         return Response(serializer.data)

class loadCategory(APIView):
    def get(self, request):
        BASE = os.path.dirname(os.path.abspath(__file__))
        f = open(os.path.join(BASE, "category.txt"))
        for record in f:
            data = record.split(':')
            _, created = Category.objects.get_or_create(
                category=data[0]
            )
            subcate = data[1].split(',')
            for subcategory in subcate:
                _, sub = Subcategory.objects.get_or_create(
                    category_id=getattr(created, 'category_id'),
                    subcategory=subcategory[0]
                )
        return Response("")

class load(APIView):
    def get(self, request):
        BASE = os.path.dirname(os.path.abspath(__file__))
        Product.objects.all().delete()
        f = open(os.path.join(BASE, "data.txt"))
        for record in f:
            data = record.split(';')
            _, created = Product.objects.get_or_create(
                product_name=data[1],
                product_short_name= data[0],
                product_make=data[4],
                product_category=data[2],
                product_subcategory=data[3],
                price=data[5],
                description=data[6],
                features=data[7],
                image_link=data[8],
            )
        return Response("")



def get_subcategories_given_categories(request):
    if request.method == 'GET' and request.is_ajax():
        category = request.GET.get("category")
        categorydb = Category.objects.filter(name__contains=category)
        subcategories = Subcategory.objects.all().filter(category_id=categorydb)
        subs = []
        for sub in subcategories:
            subs.append(sub.name)

        data = {'data': subs}
        return HttpResponse(json.dumps(data))

    raise Http404

def add_product(request):
    if(request.is_ajax() and request.method == 'POST'):
        id = request.POST.get("id")
        quantity = request.POST.get("quantity")
        id = str(id.encode('ascii', 'ignore'))
        quantity = int(quantity.encode('ascii', 'ignore'))
        basket = request.session['basket']

        if id in basket:
            basket[id] = basket[id] + quantity
            if basket[id] > 9:
                basket[id] = 9
        else:
            basket[id] = quantity

        request.session['basket'] = basket

        return HttpResponse("added product!")
    raise Http404

def change_quantity_in_basket(request):
    if (request.is_ajax() and request.method == 'POST'):
        id = request.POST.get("id")
        quantity = request.POST.get("quantity")
        id = str(id.encode('ascii', 'ignore'))
        quantity = int(quantity.encode('ascii', 'ignore'))
        basket = request.session['basket']
        basket[id] = quantity
        if(quantity == 0):
            del basket[id]

        request.session['basket'] = basket

        return HttpResponse("changed quantity!")
    raise Http404


def get_basket(request):
    if(request.is_ajax()):
        return HttpResponse(len(request.session.get("basket")))
    raise Http404

def basket(request):
    request.session['basket'] = {}

    return HttpResponse("basket resetted")

def register(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        street = request.POST.get('street')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        country = request.POST.get('country')
        postcode = request.POST.get('postcode')


        user = User(name=name, email=email, password=password, street_address=street,
                    phone_number=phone, city=city, country=country, post_code=postcode)

        user.save()

        return HttpResponseRedirect("/account/registered")

def checkemail(request):
    if (request.is_ajax() and request.method == 'POST'):
        email = request.POST.get("email")
        try:
            User.objects.get(email=email)
            return HttpResponse("invalid")
        except User.DoesNotExist:
            return HttpResponse("valid")

def logout(request):
    if (request.is_ajax() and request.method == 'POST'):
        del request.session['account']
    return HttpResponse()