from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre   = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20, default='SOME STRING')
    direccion     = models.CharField(max_length=20)
    telefono     = models.CharField(max_length=10)
    ocupacion     = models.CharField(max_length=20)
    edad  = models.IntegerField()
    correo  = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre