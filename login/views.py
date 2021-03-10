from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import auth

from . import views

# Create your views here.


def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')
def handleLogin(request):
    if request.method=='POST':
        name=request.POST['name']
        password1=request.POST['password']
        
        user=auth.authenticate(username=name,password=password1)

        if user is not None:
            
            messages.success(request,"Successfully Logged In")
            return render(request,'dashboard.html')
        else:
            messages.success(request,"Invalid username or password,Please try again")
    
    return render(request,'login.html')

def AboutUs(request):
    return render(request,'us.html')
def dashboard(request):
    return render(request,'dashboard.html')