from django.db import models
from apps.empleados.models import Employee
from apps.utils.mixins import AuditMixin


class ImprovementPlan(AuditMixin, models.Model):
    STATUS_CHOICES = [
        ("open",        "Abierto"),
        ("in_progress", "En Progreso"),
        ("closed",      "Cerrado"),
    ]

    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class ActionItem(AuditMixin, models.Model):
    plan        = models.ForeignKey(ImprovementPlan, related_name="actions", on_delete=models.CASCADE)
    description = models.TextField()
    responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    due_date    = models.DateField()
    completed   = models.BooleanField(default=False)
    evidence    = models.FileField(upload_to="improvement_evidence/", blank=True, null=True)
    comments    = models.TextField(blank=True)
    closed_at   = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-due_date"]

    def __str__(self) -> str:
        return f"{self.plan.title}: {self.description[:50]}"


class RiskAction(AuditMixin, models.Model):
    risk_assessment = models.ForeignKey(
        "riesgos.RiskAssessment", on_delete=models.CASCADE, related_name="actions"
    )
    description  = models.TextField()
    responsible  = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    due_date     = models.DateField()
    completed    = models.BooleanField(default=False)
    evidence     = models.FileField(upload_to="risk_actions_evidence/", blank=True, null=True)
    comments     = models.TextField(blank=True)
    closed_at    = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.risk_assessment}: {self.description[:40]}"
