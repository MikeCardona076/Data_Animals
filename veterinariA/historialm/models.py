from django.db import models

# Create your models here.
class Historialm(models.Model):
    tipo_operacion   = models.TextField()
    #date_income = models.DateTimeField(auto_now_add=True)
    observaciones    = models.TextField()
    
    def __str__(self):
        return self.tipo_operacion
    


class Historial(models.Model):
    operacion = models.CharField(max_length=20)
    fecha_entrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.operacion