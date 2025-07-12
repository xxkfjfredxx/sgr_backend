# apps/empresa/models.py
from django.db import models
from apps.tenants.models import Tenant
from django.db import connection
from django_tenants.models import TenantMixin
from django.core.exceptions import ValidationError
import re
import logging

# Configura el logger
logger = logging.getLogger(__name__)

class Company(TenantMixin, models.Model):
    name = models.CharField(max_length=150)
    nit = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    schema_name = models.CharField(max_length=63, unique=True)
    domain_url = models.CharField(max_length=128, unique=True)
    is_deleted = models.BooleanField(default=False)
    auto_create_schema = True  # importante para django-tenants

    class Meta:
        db_table = "companies"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.schema_name:
            clean_name = re.sub(r'[^a-z0-9]', '', self.name.lower())
            clean_nit = re.sub(r'[^0-9]', '', self.nit)
            generated_schema = f"{clean_name}_{clean_nit}"[:63]

            if Company.objects.filter(schema_name=generated_schema).exists():
                raise ValidationError("Ya existe una empresa con este schema generado. Cambia el nombre o NIT.")

            self.schema_name = generated_schema

        if not self.domain_url:
            self.domain_url = f"{self.schema_name}.localhost"

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        from django_tenants.utils import schema_context, get_tenant_model, get_public_schema_name
        from django.db import connection

        # Evita que alguien borre el esquema público
        if self.schema_name == get_public_schema_name():
            raise ValidationError("No puedes eliminar el esquema público.")

        schema_name = self.schema_name

        super().delete(*args, **kwargs)  # ← borra el tenant del modelo

        # Elimina el schema físico (solo si no es public)
        with connection.cursor() as cursor:
            cursor.execute(f'DROP SCHEMA IF EXISTS "{schema_name}" CASCADE;')

    def soft_delete(self):
        self.is_deleted = True
        self.is_active = False
        self.save()
