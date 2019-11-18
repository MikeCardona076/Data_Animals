from django.contrib import admin
from .models import Mascota

# Register your models here.
@admin.register(Mascota)

class MascotaAdmin(admin.ModelAdmin):
    list_display = [
    "id",
    "nombre_mascota",
    "raza",
    "especie"
  
    ]
