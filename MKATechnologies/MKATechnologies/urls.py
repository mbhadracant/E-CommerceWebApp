"""MKATechnologies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from django.contrib import admin
from website import views
from product.models import Category
from accounts import views as accountviews



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^api/', include('product.urls')),
    url(r'^search/$', views.search),
    url(r'^product/([0-9]{1,4})/$', views.product),
    url(r'^account/$', views.account),
    url(r'^account/(?P<error>\w+)$', views.account),
    url(r'^basket/$', views.basket),
    url(r'^checkout/$', views.checkout),
    url(r'^checkout/1/$', views.checkout_delivery),
    url(r'^checkout/2/$', views.checkout_payment),
    url(r'^checkout/3/$', views.checkout_confirm),
    url(r'^checkout/4/$', views.checkout_success),
    url(r'^account/login/$', accountviews.login),

]

categories = Category.objects.all()

for category in categories:
    urlpatterns.append(url(r'^(?P<url_name>(' + category.url_name + '))/$', views.department))


urlpatterns = format_suffix_patterns(urlpatterns)
