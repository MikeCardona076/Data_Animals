from django.db import models

# Create your models here.
class Vacunas(models.Model):
    tipo_vacuna   = models.CharField(max_length=20)
    fecha     = models.DateField()

    def __str__(self):
        return self.tipo_vacuna