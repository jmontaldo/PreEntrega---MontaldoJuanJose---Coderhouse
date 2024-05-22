from django.shortcuts import render, redirect, HttpResponse
from Clientes.models import Clientes
from Clientes.forms import ClienteForm

def clientes(request):
    consulta = Clientes.objects.all()
    contexto = {"pasajeros": consulta}
    return render(request, "Clientes/pasajeros.html", contexto)

def cliente_buscar(request):
    return render(request, "Clientes/pasajeros_busqueda.html")

def buscar(request):
    if request.GET['apellido']:
        apellido = request.GET['apellido']
        clientes = Clientes.objects.filter(apellido__icontains = apellido)
        contexto = {"pasajeros": clientes}
        return render(request, "Clientes/resultados_busqueda.html", contexto)
    else:
        respuesta = ""
        contexto = {"pasajeros": respuesta}
        return render(request, "Clientes/resultados_busqueda.html", contexto)

def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes:clientes")
    else:
        form = ClienteForm()
    return render(request, "Clientes/pasajeros_create.html", {"form":form})

def cliente_eliminar(request, documento: int):
    cliente = Clientes.objects.get(numero_documento = documento)
    cliente.delete()
    consulta = Clientes.objects.all()
    contexto = {"pasajeros": consulta}
    return render(request, "Clientes/pasajeros.html", contexto)

def cliente_update(request, documento: int):
    cliente = Clientes.objects.get(numero_documento = documento)
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            cliente.nombre = informacion["nombre"]
            cliente.apellido = informacion["apellido"]
            cliente.numero_documento = informacion["numero_documento"]
            cliente.save()
            return redirect("clientes:clientes")
    else:
        form = ClienteForm(initial={"nombre":cliente.nombre, "apellido":cliente.apellido, "numero_documento":cliente.numero_documento})
    return render(request, "Clientes/pasajeros_update.html", {"form":form, "pasajeros": documento})