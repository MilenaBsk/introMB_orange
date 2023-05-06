from django.contrib import admin
from django.urls import path
from links import views



urlpatterns = [
    path('first/', views.first, name='first_name'),
    path('second/', views.second, name='second_name'),
    path('third/<str:param>/', views.third_view, name= 'third_name')
    ]