from django.db import models
 
from apps.empresa.models import Company
from apps.utils.mixins import AuditMixin


class Branch(AuditMixin, models.Model):  # Sucursal
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "branches"
        ordering = ["name"]
        unique_together = (("name", "company"),)

    def __str__(self):
        return self.name


class Position(AuditMixin, models.Model):  # Cargo
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    RISK_LEVEL_CHOICES = [
        ("bajo", "Bajo"),
        ("medio", "Medio"),
        ("alto", "Alto"),
    ]
    risk_level = models.CharField(max_length=10, choices=RISK_LEVEL_CHOICES)

    class Meta:
        db_table = "positions"
        ordering = ["name"]
        unique_together = (("name", "company"),)

    def __str__(self):
        return self.name


class WorkArea(AuditMixin, models.Model):  # Área
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "work_areas"
        ordering = ["name"]
        unique_together = (("name", "company"),)

    def __str__(self):
        return self.name
