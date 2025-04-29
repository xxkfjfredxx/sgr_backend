# apps/cambios/models.py
from django.db import models
from apps.utils.mixins import AuditMixin
from apps.usuarios.models import User
from apps.empleados.models import Employee  # si lo necesitas para implemented_by


class ChangeRequest(AuditMixin, models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("approved", "Aprobado"),
        ("rejected", "Rechazado"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending", db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["status"]), models.Index(fields=["is_deleted"])]

    def __str__(self):
        return f"{self.title} ({self.status})"


class ChangeEvaluation(AuditMixin, models.Model):
    change_request = models.OneToOneField(
        ChangeRequest, on_delete=models.CASCADE, related_name="evaluation"
    )
    evaluated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    evaluation_comments = models.TextField()
    risk_level = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)
    evaluated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-evaluated_at"]

    def __str__(self):
        return f"Evaluación {self.change_request} – {self.risk_level}"


class ChangeImplementation(AuditMixin, models.Model):
    change_request = models.OneToOneField(
        ChangeRequest, on_delete=models.CASCADE, related_name="implementation"
    )
    implemented_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True
    )
    implementation_date = models.DateField()
    verification_comments = models.TextField(blank=True)
    verified_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="change_verifications",
    )
    verification_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-implementation_date"]

    def __str__(self):
        return f"Implementación {self.change_request} – {self.implementation_date}"
