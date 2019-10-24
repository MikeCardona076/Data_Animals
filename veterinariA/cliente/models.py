from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre   = models.CharField(max_length=20)
    direccion     = models.CharField(max_length=20)
    telefono     = models.IntegerField()
    ocupacion     = models.CharField(max_length=20)
    edad  = models.IntegerField()
    correo  = models.CharField(max_length=30)