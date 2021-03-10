from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
urlpatterns = [
        
        path('login', views.login, name='login'),
        path('handleLogin', views.handleLogin, name='handleLogin'),
        path('AboutUs', views.AboutUs, name='AboutUs'),
         path('dashboard', views.dashboard, name='dashboard'),
           path('home', views.home, name='home'),

  
]