from rest_framework import serializers
from .models import Products
from .models import Orders

class ProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField()
    product_category = serializers.CharField()
    price = serializers.IntegerField()
    colour = serializers.CharField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance

class OrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(read_only=True)
    user_id = serializers.CharField()
    product_id = serializers.IntegerField()
    total = serializers.IntegerField()

    def create(self, validated_data):
        return Orders.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance