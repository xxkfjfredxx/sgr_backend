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
