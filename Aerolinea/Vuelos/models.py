from django.db import models

class Vuelos(models.Model):
    codigo = models.IntegerField(unique=True, blank= False, verbose_name="Código")
    origen = models.CharField(max_length=100, blank= False)
    destino = models.CharField(max_length=100, blank= False)

    def __str__(self) -> str:
        return f"{self.codigo}, {self.origen}, {self.destino}"
    
class Destinos(models.Model):
    nombre = models.CharField(max_length=100, blank= False)
    descripcion = models.TextField(blank= False, verbose_name="Descripción")

    def __str__(self) -> str:
        return f"{self.nombre}, {self.descripcion}"
    
