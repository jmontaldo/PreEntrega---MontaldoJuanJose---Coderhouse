from django.contrib import admin
from django.urls import path
from .views import inicio, about, registrar_usuario, CustomLoginView, LogoutView

app_name = "core"

urlpatterns = [
    path("", inicio, name='inicio'),
    path("About/", about, name='about'),
    path("Login/", CustomLoginView.as_view(), name="login"),
    path("Registrar/", registrar_usuario, name='registrar'),
    path("Logout/", LogoutView.as_view(template_name='Core/logout.html'), name='logout'),
]