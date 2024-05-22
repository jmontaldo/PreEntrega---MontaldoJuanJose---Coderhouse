from django.contrib import admin
from django.urls import path
from .views import vuelos, vuelos_create, vuelos_destino, vuelos_buscar, buscar

app_name = "vuelos"

urlpatterns = [
    path("", vuelos, name='vuelos'),
    path("Search/", vuelos_buscar, name='search'),
    path("Search/Destino", buscar, name='vuelo_search'),
    path("Create/", vuelos_create, name='create'),
    path("Vuelos_Destino/<int:pk>", vuelos_destino, name='vuelos_destino'),
]