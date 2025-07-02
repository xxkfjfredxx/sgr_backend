from django.db import models
from apps.core.models import TenantBase
from apps.utils.mixins import AuditMixin


class ContractorCompany(TenantBase,AuditMixin, models.Model):
    name = models.CharField(max_length=150)
    nit = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ContractorContact(AuditMixin, models.Model):
    contractor = models.ForeignKey(
        ContractorCompany, on_delete=models.CASCADE, related_name="contacts"
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    position = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.contractor.name})"
