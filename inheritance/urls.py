from django.urls import path

from inheritance import views

app_name = 'iheritance'

urlpatterns = [
    path('first/', views.first_view, name='first_name')
]