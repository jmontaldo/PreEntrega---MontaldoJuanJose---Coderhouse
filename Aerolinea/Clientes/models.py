from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=100, blank= False)
    apellido = models.CharField(max_length=100, blank= False)
    numero_documento = models.IntegerField(unique= True, blank= False)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}, {self.numero_documento}"
