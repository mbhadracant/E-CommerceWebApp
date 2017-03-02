from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    product_id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length=200)
    product_make = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)

class Product_option(models.Model):
    option_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    option = models.CharField(max_length=200)
    price = models.IntegerField()

class Users(models.Model):
    username = models.CharField(max_length=200, primary_key = True)
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
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_id= models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=200)
    total = models.IntegerField(max_length=200)

