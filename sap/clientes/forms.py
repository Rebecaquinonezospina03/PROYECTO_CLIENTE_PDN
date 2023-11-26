from django.forms import ModelForm, EmailInput
from django.forms import ModelForm
from django import forms
from clientes.models import Cliente, Producto, Pedido


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'correo', 'telefono', 'direccion', 'fecha_nacimiento', 'tipo_producto', 'numero_de_pedido',
                  'activo']
        widgets = {
            'email': forms.EmailInput(attrs={'type': 'email'}),
            'Fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
