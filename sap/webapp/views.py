from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from clientes.models import Cliente


# Create your views here.
def bienvenida2(request):
    cantidadclientes = Cliente.objects.count()
    clientes = Cliente.objects.order_by('apellido', 'nombre')
    dict_datos = {'cantidadclientes': cantidadclientes, 'clientes': clientes}
    pagina = loader.get_template('bienvenida.html')
    return HttpResponse(pagina.render(dict_datos, request))
