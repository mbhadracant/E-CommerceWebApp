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

def login(request):
    return render(request, 'website/account.html')

def account(request):

    return render(request, 'website/account-logged-in.html')
