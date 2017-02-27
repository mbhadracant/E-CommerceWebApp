from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    options = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)

class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class Orders(models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    productID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField(max_length=200)
    Total = models.IntegerField(max_length=200)
