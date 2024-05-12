from django.db import models

class Vuelos(models.Model):
    codigo = models.IntegerField(unique=True, blank= False)
    origen = models.CharField(max_length=100, blank= False)
    destino = models.CharField(max_length=100, blank= False)

    def __str__(self) -> str:
        return f"{self.codigo}, {self.origen}, {self.destino}"
