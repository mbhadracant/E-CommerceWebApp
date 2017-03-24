from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from product.models import Category, Subcategory

def index(request):
    return render(request, 'website/index.html')

def department(request, url_name):
    category_id = Category.objects.all().filter(url_name=url_name)
    subcategories = Subcategory.objects.all().filter(category_id=category_id)
    name = Category.objects.get(category_id=category_id)

    context = {'subcategories' : subcategories,
               'category_url_name': url_name,
               'category_full_name': name,
               }


    return render(request, 'website/department.html', context)

def search(request):
    return render(request, 'website/search.html')

def product(request):
    return render(request, 'website/product.html')

def account(request, error=None):
    context = {}
    if error:
        context['error_message'] = 'Incorrect email or password entered'
    return render(request, 'website/account.html', context)

def checkout_delivery(request):
    context = {}
    return render(request, 'website/checkout-delivery.html', context)

def checkout_payment(request):
    context = {}
    return render(request, 'website/checkout-payment.html', context)

def checkout_confirm(request):
    context = {}
    return render(request, 'website/checkout-confirm.html', context)

def checkout_success(request):
    context = {}
    return render(request, 'website/checkout-success.html', context)

def checkout(request):
    context = {}
    return HttpResponseRedirect("/checkout/1")


def basket(request):
    context = {}
    return render(request, 'website/basket.html',context)
