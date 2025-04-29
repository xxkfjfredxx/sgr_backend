from django.db import models
from apps.utils.mixins import AuditMixin


class Company(AuditMixin, models.Model):
    name    = models.CharField(max_length=150)
    nit     = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone   = models.CharField(max_length=20,  blank=True, null=True)
    email   = models.EmailField(blank=True, null=True)
    sector  = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "companies"
        ordering = ["name"]

    def __str__(self):
        return self.name
