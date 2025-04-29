from django.db import models
from apps.utils.mixins import AuditMixin


class Branch(AuditMixin, models.Model):           # Sucursal
    name    = models.CharField(max_length=100, unique=True)
    address = models.TextField(blank=True, null=True)
    city    = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table  = "branches"
        ordering  = ["name"]

    def __str__(self):
        return self.name


class Position(AuditMixin, models.Model):         # Cargo
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table  = "positions"
        ordering  = ["name"]

    def __str__(self):
        return self.name


class WorkArea(AuditMixin, models.Model):         # Área
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table  = "work_areas"
        ordering  = ["name"]

    def __str__(self):
        return self.name
