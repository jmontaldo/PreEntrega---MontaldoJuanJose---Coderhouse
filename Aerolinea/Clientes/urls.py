from django.contrib import admin
from django.urls import path
from .views import clientes, cliente_create, cliente_eliminar, cliente_update, cliente_buscar, buscar

app_name = "clientes"

urlpatterns = [
    path("", clientes, name='clientes'),
    path("Search/", cliente_buscar, name= 'search'),
    path("Search/Cliente", buscar, name='clientsearch'),
    path("Create/", cliente_create, name='create'),
    path("Delete/<int:documento>", cliente_eliminar, name='delete'),
    path("Update/<int:documento>", cliente_update, name='update'),
]