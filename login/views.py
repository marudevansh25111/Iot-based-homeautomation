from django.shortcuts import render

from . import views

# Create your views here.


def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def AboutUs(request):
    return render(request,'us.html')
def dashboard(request):
    return render(request,'dashboard.html')