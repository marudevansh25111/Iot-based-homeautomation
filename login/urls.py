from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
urlpatterns = [
        
        path('login', views.login, name='login'),
        path('home', views.home, name='home'),
        path('AboutUs', views.AboutUs, name='AboutUs'),
        
  
]