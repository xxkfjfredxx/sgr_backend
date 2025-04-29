from django.db import models
from apps.utils.mixins import AuditMixin
from apps.empleados.models import Employee


class SuggestionBox(AuditMixin, models.Model):
    TYPE_CHOICES = [
        ("Sugerencia", "Sugerencia"),
        ("Queja",      "Queja"),
        ("Reporte",    "Reporte de Condición Insegura"),
        ("Mejora",     "Propuesta de Mejora"),
        ("Otro",       "Otro"),
    ]

    employee    = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    type        = models.CharField(max_length=30, choices=TYPE_CHOICES)
    title       = models.CharField(max_length=150)
    description = models.TextField()
    anonymous   = models.BooleanField(default=False)
    response    = models.TextField(blank=True)
    responded   = models.BooleanField(default=False)
    responded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.type}: {self.title}"
