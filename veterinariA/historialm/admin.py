from django.contrib import admin

from .models import Historialm

# Register your models here.
@admin.register(Historialm)

class HistorialmAdmin(admin.ModelAdmin):
    list_display = [
    "id",
    "observaciones"

    ]