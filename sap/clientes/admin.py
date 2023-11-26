from django.contrib import admin

# Register your models here.
from .models import Cliente, Producto, Pedido

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)