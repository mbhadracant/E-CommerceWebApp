from rest_framework import serializers
from .models import Products
from .models import Orders
from .models import Users

class OrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    product_id = ProductSerializer()
    user_id = UserSerializer()
    quantity = serializers.IntegerField()
    total = serializers.IntegerField()

    class Meta:
        model = Orders
        fields = ('order_id', 'product_id', 'user_id')

    def create(self, validated_data):
        return Orders.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance