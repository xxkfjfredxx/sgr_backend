from django.db import models
from django_multitenant.models import TenantModel
from django_multitenant.utils import get_current_tenant

class TenantBase(TenantModel):
    # Nombre del campo que usa django_multitenant para filtrar
    tenant_id = "company_id"

    # Relación al modelo Company de tu app
    company   = models.ForeignKey(
        "empresa.Company",
        on_delete=models.PROTECT,
        help_text="Empresa/tenant al que pertenece este registro",
    )

    class Meta:
        abstract = True  # No crea tabla propia

    def save(self, *args, **kwargs):
        # Antes de guardar, si no hay company asignada,
        # la toma de la sesión/contexto actual
        if not self.company_id:
            self.company = get_current_tenant()
        super().save(*args, **kwargs)
