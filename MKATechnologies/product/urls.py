from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/$', views.ProductList.as_view()),
    url(r'^product/product_id$', views.ProductDetails.as_view()),
    url(r'^product/product_category$', views.ProductCategory.as_view()),
    url(r'^product/brand$', views.ProductBrand.as_view()),
    url(r'^order/$', views.OrderList.as_view()),
    url(r'^order/order_id$', views.OrderDetails.as_view()),
    url(r'^order/user_id$', views.UserOrderDetails.as_view()),
    # url(r'^account/user_id$', views.UserDetails.as_view()),
    url(r'^load/$', views.load.as_view()),
    url(r'^loadCategory/$', views.loadCategory.as_view()),
    url(r'^subcategories/$', views.get_subcategories_given_categories),
    url(r'^getproducts/$', views.get_products),
    url(r'^addproduct/$', views.add_product),
    url(r'^changequantity/$', views.change_quantity_in_basket),
    url(r'^checkemail/$', views.checkemail),
    url(r'^register/$', views.register),
    url(r'^getbasket/$', views.get_basket),
    url(r'^basket/$', views.basket),
    url(r'^logout/$', views.logout),
]
