from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from clientes.forms import ClienteForm
from clientes.models import Cliente


# Create your views here.

def agregar_cliente(request):
    global formulario
    pagina = loader.get_template('clientes/agregar.html')
    if request.method == 'GET':
        formulario = ClienteForm
    elif request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))


def modificar_cliente(request, id):
    global formulario
    pagina = loader.get_template('clientes/modificar.html')
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'GET':
        formulario = ClienteForm(instance=cliente)
    elif request.method == 'POST':
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))


def ver_cliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    datos = {'cliente': cliente}
    print(cliente)
    pagina = loader.get_template('clientes/ver.html')
    return HttpResponse(pagina.render(datos, request))


def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if cliente:
        cliente.delete()
        return redirect('inicio')

# Create your views here.
