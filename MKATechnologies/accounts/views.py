from django.shortcuts import render, redirect
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# def home(request):
#     return render(request, 'accounts/home.html')
# 
# def index(request):
#     template = loader.get_template('accounts/index.html')
#     context = {}
# 
#     return HttpResponse(template.render(context, request))

def checklogin(request):
    email = request.GET.get('email')
    password = request.GET.get('password')

    try:
        users = Users.objects.get(email=email, password=password)
        return HttpResponse("Logged In!")
    except Users.DoesNotExist:
        return HttpResponse("Incorrect")

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

# def view_profile(request):
#     args = {'user': request.user}
#     return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
