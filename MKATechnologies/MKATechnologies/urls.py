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

departments = ['computing','tv-and-home-cinema','gaming','mobile-phones','camera']
departments_re = '(?:' + '|'.join(departments) + ')'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^api/', include('product.urls')),
    url(r'^' + departments_re + '/$', views.department),
    url(r'^search/$', views.search),
    url(r'^product/$', views.product),
    url(r'^account/$', views.account),
#     url(r'^account/$', include('accounts.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
