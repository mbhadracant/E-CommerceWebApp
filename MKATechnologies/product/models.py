from __future__ import unicode_literals
from django.db import models
from accounts.models import User

class Product(models.Model):
    product_id = models.AutoField(primary_key = True)
    product_short_name = models.CharField(max_length=40)
    product_name = models.CharField(max_length=200)
    product_make = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_subcategory = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
    description = models.CharField(max_length=400)
    features = models.CharField(max_length=400)
    image_link = models.CharField(max_length=400)

    def __str__(self):
        return "[" + self.product_short_name + " | " + self.product_make + "]"

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(max_length=200)
    name = models.CharField(max_length=200)
    total = models.FloatField(max_length=200)
    street_name = models.CharField(max_length=200)
    postcode = models.CharField(max_length=7)
    date = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class ProductOrder(models.Model):
    product_order_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    url_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    subcategory_image = models.CharField(max_length=200)

    def __str__(self):
        return self.name
