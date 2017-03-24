#hello.py
from product.models import Category, Subcategory, Product
from accounts.models import User


def run():
    category = "Computing"


    products = Product.objects.all().filter(product_category__contains="TV & Home cinema")

    for p in products:
        print(p.product_category)


