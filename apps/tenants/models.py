# apps/tenants/models.py
from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)  # Nombre del tenant
    db_label = models.CharField(max_length=100, unique=True)  # Identificador único de la base de datos para este tenant
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return self.name
