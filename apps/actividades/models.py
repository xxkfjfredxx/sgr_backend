from django.db import models
from apps.utils.mixins import AuditMixin


class Activity(AuditMixin, models.Model):
    STATUS_CHOICES = [
        ("pending",     "Pendiente"),
        ("in_progress", "En progreso"),
        ("completed",   "Finalizada"),
        ("cancelled",   "Cancelada"),
    ]

    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date  = models.DateField()
    end_date    = models.DateField(null=True, blank=True)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    class Meta:
        ordering = ["start_date"]

    def __str__(self) -> str:
        return f"{self.title} · {self.get_status_display()}"
