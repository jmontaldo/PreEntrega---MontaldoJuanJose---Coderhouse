from django import forms
from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Clientes
        fields = ["nombre", "apellido", "numero_documento"]