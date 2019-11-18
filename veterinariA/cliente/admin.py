from django.contrib import admin

from .models import Cliente

# Register your models here.
#admin.site.register(Cliente)

@admin.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = [
    "id",
    "nombre",
    "apellidos",
    "correo",
    "direccion",
    "ocupacion"


    ]