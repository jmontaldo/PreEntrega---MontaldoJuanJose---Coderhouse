from django.shortcuts import render, redirect
from Vuelos.models import Vuelos, Destinos
from Vuelos.forms import VuelosForm

def vuelos(request):
    consulta = Vuelos.objects.all()
    contexto = {"vuelos": consulta}
    return render(request, "Vuelos/vuelos.html", contexto)

def vuelos_buscar(request):
    return render(request, "Vuelos/vuelos_busqueda.html")

def buscar(request):
    if request.GET['destino']:
        destino = request.GET['destino']
        vuelos = Vuelos.objects.filter(destino__icontains = destino)
        contexto = {"vuelos": vuelos}
        return render(request, "Vuelos/resultados_busqueda.html", contexto)
    else:
        vuelos = ""
        contexto = {"vuelos": vuelos}
        return render(request, "Vuelos/resultados_busqueda.html", contexto)

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
