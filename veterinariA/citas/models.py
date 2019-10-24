from django.db import models

# Create your models here.
class Citas(models.Model):
    fecha_cita  = models.DateField()
    notas     = models.TextField()
    clinica    = models.CharField(max_length=20)
    horario    = models.DateField()
    