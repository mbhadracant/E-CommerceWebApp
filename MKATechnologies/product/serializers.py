from rest_framework import serializers
from .models import Products
from .models import Orders
from .models import Users

class ProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(read_only=True)
    product_name = serializers.CharField()
    product_category = serializers.CharField()
    product_make = serializers.CharField()
    price = serializers.IntegerField()
    colour = serializers.CharField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.IntegerField()

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance