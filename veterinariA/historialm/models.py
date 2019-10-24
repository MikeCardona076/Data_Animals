from django.db import models

# Create your models here.
class Historialm(models.Model):
    tipo_operacion   = models.TextField()
    fecha_inicio     = models.IntegerField()
    observaciones    = models.TextField()
    