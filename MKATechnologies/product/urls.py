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
]
