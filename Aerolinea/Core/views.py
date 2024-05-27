from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAutenthicationForm, CustomUserCreationForm

def inicio (request):
    return render (request, "Core/index.html")

def about(request):
    return render (request, "Core/about.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAutenthicationForm
    template_name = "Core/login.html"
    
def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Core/index.html", {"user": username})
    else:
        form = CustomUserCreationForm()
    return render(request, "Core/registrar.html", {"form": form})