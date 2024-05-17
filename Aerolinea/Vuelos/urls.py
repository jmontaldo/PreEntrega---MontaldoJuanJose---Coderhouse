from django.contrib import admin
from django.urls import path
from .views import vuelos, vuelos_create, vuelos_destino

app_name = "vuelos"

urlpatterns = [
    path("", vuelos, name='vuelos'),
    path("Create/", vuelos_create, name='create'),
    path("Vuelos_Destino/<int:pk>", vuelos_destino, name='vuelos_destino'),
]