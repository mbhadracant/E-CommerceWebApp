from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    name = serializers.CharField()
    street_address = serializers.CharField()
    email = serializers.CharField()
    city = serializers.CharField()
    country = serializers.CharField()
    post_code = serializers.CharField()
    phone_number = serializers.IntegerField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
