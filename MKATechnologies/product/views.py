from django.shortcuts import render
from rest_framework.views import APIView
from .models import Products
from .models import Orders
from .serializers import  ProductSerializer
from .serializers import OrderSerializer
from rest_framework.response import Response

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

#Get provides given the brand
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
