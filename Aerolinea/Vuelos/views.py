from django.shortcuts import render
from Vuelos.models import Vuelos

def vuelos(request):
    consulta = Vuelos.objects.all()
    contexto = {"vuelos": consulta}
    return render(request, "Core/vuelos.html", contexto)
