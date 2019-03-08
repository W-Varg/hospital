from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    carnet = models.CharField(max_length=20)
    tipo_seguro = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
