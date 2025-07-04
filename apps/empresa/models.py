# apps/empresa/models.py
from django.db import models
from django_multitenant.models import TenantModel
from apps.utils.mixins import AuditMixin
from apps.tenants.models import Tenant

class Company(TenantModel, AuditMixin, models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE) 
    
    db_label = models.CharField(max_length=100, unique=True) 
    name = models.CharField(max_length=150)
    nit = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class TenantMeta:
        tenant_field_name = "tenant_id"

    class Meta:
        db_table = "companies"
        ordering = ["name"]
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.name