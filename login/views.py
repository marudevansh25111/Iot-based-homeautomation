from django.shortcuts import render

from . import views

# Create your views here.


def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.py')

def AboutUs(request):
    return render(request,'us.html')
