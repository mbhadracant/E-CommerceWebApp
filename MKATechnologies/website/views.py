from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseBadRequest
from product.models import Category, Subcategory, Product, Order, ProductOrder
from accounts.models import User
import datetime
import smtplib
import sys
import json
print sys.getdefaultencoding()

def index(request):

    if 'basket' not in request.session:
        request.session['basket'] = {}



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


def account(request, text=None):
    context = {}
    if text:
        if(text == 'error'):
            context['error_message'] = 'Incorrect email or password entered'
        if(text == 'registered'):
            context['registered'] = "Account created"

    if('account' in request.session):
        orders = []
        id = request.session['account']['user_id']
        user = User.objects.get(user_id=id)

        orders_db = Order.objects.all().filter(user_id=user)

        for o in orders_db:

            product_orders = ProductOrder.objects.all().filter(order_id=o)

            orders.append({'order': o, 'products_order': product_orders, })
        context['orders'] = orders

        return render(request, 'website/account-logged-in.html', context)
    return render(request, 'website/account.html', context)

def checkout_delivery(request):
    context = {}
    request.session['checkout'] = {}
    return render(request, 'website/checkout-delivery.html', context)

def checkout_payment(request):
    if request.META.get('HTTP_REFERER') is not None:
        if request.method == 'POST':
            dict = request.session['checkout']
            name = request.POST.get("name")
            street = request.POST.get("street")
            postcode = request.POST.get("postcode")
            city = request.POST.get("city")
            country = request.POST.get("country")

            dict['name'] = name
            dict['street'] = street
            dict['postcode'] = postcode
            dict['city'] = city
            dict['country'] = country

            request.session['checkout'] = dict

            context = {}
            return render(request, 'website/checkout-payment.html', context)
    return HttpResponseBadRequest("Invalid request")

def checkout_confirm(request):
    if request.META.get('HTTP_REFERER') is not None:
        if request.method == 'POST':
            dict = request.session['checkout']
            cardnumber = request.POST.get("cardnumber")
            expiry = request.POST.get("expiry")
            cardholdername = request.POST.get("cardholdername")

            dict['cardnumber'] = cardnumber
            dict['expiry'] = expiry
            dict['cardholdername'] = cardholdername

            request.session['checkout'] = dict

            products = []
            total = 0
            basket = request.session['basket']

            for key, value in basket.items():
                id = int(key)
                quantity = value

                product = Product.objects.get(product_id=id)
                price = float(product.price) * float(quantity)
                products.append({'quantity': quantity, 'product': product, 'price': price})
                total += price

            context = {'products' : products, 'total' : total}

            return render(request, 'website/checkout-confirm.html', context)
    return HttpResponseBadRequest("Invalid request")

def checkout_success(request):
    if request.META.get('HTTP_REFERER') is not None:
        if request.method == 'POST':
            basket = request.session['basket']
            user_id = request.session['account']['user_id']
            user = User.objects.get(user_id = user_id)
            name = request.session['checkout']['name']
            total = request.session['basket_total']
            street = request.session['checkout']['street']
            postcode = request.session['checkout']['street']
            city = request.session['checkout']['city']
            country = request.session['checkout']['country']
            date = datetime.datetime.today().strftime('%d-%m-%Y')

            order = Order(user_id=user, name=name, total = total, street_name=street,
                          postcode=postcode, city=city, country=country, date=date)
            order.save()
            msg_template = ""
            for key,value in basket.items():
                    product = Product.objects.get(product_id=int(key))
                    product_order = ProductOrder(order_id=order,
                                                 product_id=product, quantity=value)
                    product_order.save()
                    msg_template = msg_template + str(value) + "x " + product.product_name + " - "\
                                 + str(product.price * float(value)) + " \n"


            context = {}


            fromaddr = 'mka.tech.helpdesk@gmail.com'
            toaddrs = request.session['account']['email']
            msg = 'Hi, ' + request.session['account']['name'] + "\n\nHere is your order:\n\n"
            msg = msg + msg_template
            msg = msg + "-----------------------------"
            msg = msg + "\nTotal: " + str(total) + "\n\nThanks for shopping with us,\nMKA Technologies"
            username = 'mka.tech.helpdesk@gmail.com'
            password = 'adminmka'
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()

            request.session['basket'] = {}


            return render(request, 'website/checkout-success.html', context)
    return HttpResponseBadRequest("Invalid request")

def checkout(request):
    context = {}
    return HttpResponseRedirect("/checkout/1")


def basket(request):

    products = []
    total = 0
    basket = request.session['basket']

    for key,value in basket.items():
        id = int(key)
        quantity = value

        product = Product.objects.get(product_id=id)
        price = float(product.price) * float(quantity)
        products.append({'quantity': quantity, 'product': product, 'price':price})
        total += price

    request.session['basket_total'] = total
    context = {'products':products, 'total' : total}
    return render(request, 'website/basket.html',context)
