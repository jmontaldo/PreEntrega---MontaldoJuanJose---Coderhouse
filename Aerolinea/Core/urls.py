from django.contrib import admin
from django.urls import path
from .views import inicio

app_name = "core"

urlpatterns = [
    path("", inicio, name='inicio'),
]