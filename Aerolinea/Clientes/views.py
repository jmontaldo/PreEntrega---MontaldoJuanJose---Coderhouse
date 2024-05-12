from django.shortcuts import render, redirect
from Clientes.models import Clientes
from Clientes.forms import ClienteForm

def clientes(request):
    consulta = Clientes.objects.all()
    contexto = {"pasajeros": consulta}
    return render(request, "Core/pasajeros.html", contexto)

def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes:clientes")
    else:
        form = ClienteForm()
    return render(request, "Core/pasajeros_create.html", {"form":form})