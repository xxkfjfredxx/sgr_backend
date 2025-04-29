from django.db import models
from apps.usuarios.models import User
from apps.utils.mixins import AuditMixin


class SupportTicket(AuditMixin, models.Model):
    STATUS_CHOICES = [
        ("open",        "Abierto"),
        ("in_progress", "En progreso"),
        ("closed",      "Cerrado"),
    ]

    title        = models.CharField(max_length=150)
    description  = models.TextField()
    created_by   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to  = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name="assigned_tickets")
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class MaintenanceSchedule(AuditMixin, models.Model):
    title           = models.CharField(max_length=150)
    description     = models.TextField(blank=True)
    scheduled_date  = models.DateField()
    responsible     = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    completed       = models.BooleanField(default=False)

    class Meta:
        ordering = ["scheduled_date"]

    def __str__(self):
        return self.title


class MaintenanceRecord(AuditMixin, models.Model):
    schedule       = models.ForeignKey(MaintenanceSchedule, on_delete=models.CASCADE, related_name="records")
    performed_by   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    performed_date = models.DateField()
    comments       = models.TextField(blank=True)

    class Meta:
        ordering = ["-performed_date"]

    def __str__(self):
        return f"Rec. {self.schedule} – {self.performed_date}"
