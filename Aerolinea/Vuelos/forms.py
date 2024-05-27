from django import forms
from . import models

class VuelosForm(forms.ModelForm):
    class Meta:
        model = models.Vuelos
        fields = ["codigo", "origen", "destino", "fecha"]