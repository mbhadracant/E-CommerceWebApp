from django.contrib import admin
from .models import Product
from .models import Category
from .models import Subcategory
from .models import Order
from .models import ProductOrder
# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(ProductOrder)
