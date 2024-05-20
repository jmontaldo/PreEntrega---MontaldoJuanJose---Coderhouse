from django.contrib import admin
from django.urls import path
from .views import clientes, cliente_create, cliente_eliminar

app_name = "clientes"

urlpatterns = [
    path("", clientes, name='clientes'),
    path("Create/", cliente_create, name='create'),
    path("Delete/<int:documento>", cliente_eliminar, name='delete'),
]