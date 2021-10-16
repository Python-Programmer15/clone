from django.shortcuts import render
from django.urls import path
from pages import views


urlpatterns = [
    path('', views.HomeView, name='index'),
]