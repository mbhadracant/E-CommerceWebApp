import csv

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from .models import Category
from .models import Subcategory
from .models import Order
from .serializers import  ProductSerializer
from .serializers import  OrderSerializer
from rest_framework.response import Response
import os

class search(APIView):
    def get(self, request):
        allProducts = Product.objects.all()
        if request.GET.get('category') is not None:
            allProducts = allProducts.filter(product_category=request.GET.get('category'))
        if request.GET.get('brand') is not None:
            allProducts = allProducts.filter(product_make=request.GET.get('brand'))
        if request.GET.get('subcategory') is not None:
            allProducts = allProducts.filter(product_subcategory=request.GET.get('subcategory'))
        if request.GET.get('productName') is not None:
            allProducts = allProducts.filter(product_name=request.GET.get('productName'))
        serializer = ProductSerializer(allProducts, many=True)
        return Response(serializer.data)

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
        f = open(os.path.join(BASE, "data.txt"))
        for record in f:
            data = record.split(';')
            _, created = Product.objects.get_or_create(
                product_name=data[0],
                product_make=data[1],
                product_category=data[2],
                product_subcategory=data[3],
                price=data[4],
                description=data[5],
                image_link=data[6],
            )
        return Response("")
