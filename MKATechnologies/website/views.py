from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'website/index.html')

def department(request):
    return render(request, 'website/department.html')

def search(request):
    return render(request, 'website/search.html')

def product(request):
    return render(request, 'website/product.html')

def account(request):
    context = {'account': {'name' : 'Mayur'}}
    #context = None
    if context is None:
        return render(request, 'website/account.html', context)
    else:
        return render(request, 'website/account-logged-in.html', context)