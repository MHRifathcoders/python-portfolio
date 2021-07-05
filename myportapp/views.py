from django import forms
from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm, MyaccountForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.
def register(request):
    form= CreateUserForm()
    if request.method == "POST":
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(request, "Account successfully created for " + user)
            return redirect('userlogin')
    context= {'form': form}
    return render(request, 'register.html', context)

def userlogin(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user= authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('myportfolio')
        else:
            messages.info(request, 'Username or Password is incorrect')
            
    context={}
    return render(request, 'userlogin.html', context)

def userlogout(request):
    logout(request)
    return redirect('userlogin')

def myportfolio(request):
    info= Portfolio.objects.all()
    context= {'info': info}
    return render(request, 'myportfolio.html', context)

def my_account(request):
    form= MyaccountForm()
    if request.method == "POST":
        form= MyaccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your information has saved')
        
    context= {'form': form}
    return render(request, 'myaccount.html', context)