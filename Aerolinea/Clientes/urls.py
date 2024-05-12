from django.contrib import admin
from django.urls import path
from .views import clientes, cliente_create

app_name = "clientes"

urlpatterns = [
    path("", clientes, name='clientes'),
    path("Create/", cliente_create, name='create'),
]