from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
urlpatterns = [
        path('', views.index, name='index'),
	path('new', views.index, name='index'),
        path('add', views.addstudentinfo, name='add'),
        path('view', views.getstudentinfo, name='add'),
        path('print', views.printinfo, name='print'),
        path('login', views.login, name='login'),
        path('home', views.home, name='home'),
        url('students', views.StudentListView.as_view(), name ='students'),
]