from django.contrib import admin
from django.urls import path
from .views import vuelos, vuelos_create

app_name = "vuelos"

urlpatterns = [
    path("", vuelos, name='vuelos'),
    path("Create/", vuelos_create, name='create'),
]