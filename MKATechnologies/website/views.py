from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from product.models import Category, Subcategory, Product

def index(request):

    if 'basket' in request.session:
        basket = request.session['basket']
        print(basket)
    else:
        request.session['basket'] = []



    return render(request, 'website/index.html')

def department(request, url_name):
    category_id = Category.objects.all().filter(url_name=url_name)
    subcategories = Subcategory.objects.all().filter(category_id=category_id)
    name = Category.objects.get(category_id=category_id)
    products = Product.objects.all().filter(product_category__contains=name)

    context = {'subcategories' : subcategories,
               'category_url_name': url_name,
               'category_full_name': name,
               'products': products
               }


    return render(request, 'website/department.html', context)

def search(request):
    return render(request, 'website/search.html')

def product(request, id):

    try:
        product = Product.objects.get(product_id=id)
        context = {'product_id': id, 'product': product}
        return render(request, 'website/product.html', context)
    except Product.DoesNotExist:
        raise Http404


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

    products = []

    basket = request.session['basket']

    for p in basket:
        product = Product.objects.get(product_id=p[0])
        products.append({'quantity': p[1], 'product': product})

    context = {'products':products}
    return render(request, 'website/basket.html',context)
