from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre_mascota   = models.CharField(max_length=20, default='SOME STRING')
    raza     = models.CharField(max_length=20)
    sexo     = models.CharField(max_length=20)
    edad     = models.IntegerField()
    vacunas_mascota  = models.TextField()
    especie  = models.CharField(max_length=20, default='SOME STRING')
    
   
    
