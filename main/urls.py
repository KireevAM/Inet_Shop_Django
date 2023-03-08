"""main URL Configuration"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index, name='index')
    path('admin/', admin.site.urls),
]
