from rest_framework import serializers
from .models import Product
from .models import Order
from .models import User
from accounts.serializer import UserSerializer

class ProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField()
    product_category = serializers.CharField()
    product_make = serializers.CharField()
    price = serializers.IntegerField()
    colour = serializers.CharField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance

class OrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    product_id = ProductSerializer()
    user_id = UserSerializer()
    quantity = serializers.IntegerField()
    total = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ('order_id', 'product_id', 'user_id')

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
