from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product/$', views.ProductList.as_view()),
    url(r'^product/product_id$', views.ProductDetails.as_view()),
    url(r'^product/product_category$', views.ProductCategory.as_view()),
    url(r'^product/brand$', views.ProductBrand.as_view()),
    url(r'^order/$', views.OrderList.as_view()),
    url(r'^order/order_id$', views.OrderDetails.as_view()),
    url(r'^search/$', views.search.as_view()),
]