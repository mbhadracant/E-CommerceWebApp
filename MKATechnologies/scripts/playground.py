#hello.py
from product.models import Category, Subcategory, Product
from accounts.models import User


def run():
    users = User.objects.all()

    for user in users:
        print(user.first_name)


