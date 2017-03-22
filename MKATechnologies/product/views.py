import csv

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Products
from .models import Orders
from .serializers import  ProductSerializer
from rest_framework.response import Response
import os

class search(APIView):
    def get(self, request):
        allProducts = Products.objects.all()
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
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

#Get product details given a product id
class ProductDetails(APIView):
    def get(self, request):
        product = Products.objects.get(product_id=request.GET.get(''))
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

#Get products given the category
class ProductCategory(APIView):
    def get(self, request):
        products = Products.objects.filter(product_category=request.GET.get(''))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

#Get all the products given the brand
class ProductBrand(APIView):
    def get(self, request):
        products = Products.objects.filter(product_make=request.GET.get(''))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class OrderList(APIView):
    def get(self, request):
        orders = Orders.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class OrderDetails(APIView):
    def get(self, request):
        order = Orders.objects.get(order_id=request.GET.get(''))
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)

class UserOrderDetails(APIView):
    def get(self, request):
        orders = Orders.objects.filter(user_id=request.GET.get(''))
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

#Get user details given user id
class UserDetails(APIView):
    def get(self, request):
        user = Users.objects.get(username=request.GET.get(''))
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

class load(APIView):
    def get(self, request):
        BASE = os.path.dirname(os.path.abspath(__file__))
        # with open(os.path.join(BASE, "data.txt")) as f:
        #     reader = csv.reader(f)
        #     for row in reader:
        #         _, created = Products.objects.get_or_create(
        #             product_name=row[0],
        #             product_make=row[1],
        #             product_category=row[2],
        #             product_sub_category=row[3],
        #             price=row[4],
        #             colour=row[5],
        #             description=row[6], image_link=row[7], quantity=row[8]
        #         )

        f = open(os.path.join(BASE, "data.txt"))
        for record in f:
            data = record.split(';')
            # _, created = Products.objects.get_or_create (
            #     product_name=record[0],
            #     product_make=record[1],
            #     product_category=record[2],
            #     product_subcategory=record[3],
            #     price=record[4],
            #     description=record[5],
            #     image_link=record[6],
            #     quantity=record[7]
            # )
        #

            _, created = Products.objects.get_or_create(
                product_name=data[0],
                product_make=data[1],
                product_category=data[2],
                product_subcategory=data[3],
                price=data[4],
                description=data[5],
                image_link=data[6],
            )
        return Response("")
