from django.contrib import admin
from django.urls import path
from .views import vuelos

app_name = "vuelos"

urlpatterns = [
    path("", vuelos, name='vuelos'),
]