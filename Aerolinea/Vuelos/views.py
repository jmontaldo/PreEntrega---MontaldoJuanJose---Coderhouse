from django.shortcuts import render, redirect
from Vuelos.models import Vuelos, Destinos
from Vuelos.forms import VuelosForm

def vuelos(request):
    consulta = Vuelos.objects.all()
    contexto = {"vuelos": consulta}
    return render(request, "Vuelos/vuelos.html", contexto)

def vuelos_create(request):
    if request.method == "POST":
        form = VuelosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vuelos:vuelos")
    else:
        form = VuelosForm()
    return render(request, "Vuelos/vuelos_create.html", {"form":form})

def vuelos_destino(request, pk: int):
    consulta = Destinos.objects.get(id=pk)
    contexto = {"vuelos_destino": consulta}
    return render(request, "Vuelos/vuelos_destino.html", contexto)
