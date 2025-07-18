from django.db import models
from apps.empleados.models import Employee
from apps.empresa.models import Company
from apps.tenants.models import Tenant
from apps.utils.mixins import AuditMixin


class ImprovementPlan(AuditMixin, models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ("open", "Abierto"),
        ("in_progress", "En Progreso"),
        ("closed", "Cerrado"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")

    class Meta:
        db_table = "improvement_plans"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class ActionItem(AuditMixin, models.Model):
    plan = models.ForeignKey(ImprovementPlan, on_delete=models.CASCADE, db_index=True)
    responsible = models.ForeignKey(
        "empleados.Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True,
    )
    description = models.TextField()
    due_date = models.DateField(db_index=True)
    completed = models.BooleanField(default=False, db_index=True)
    evidence = models.FileField(
        upload_to="improvement_evidence/", blank=True, null=True
    )
    comments = models.TextField(blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "action_items"
        ordering = ["-due_date"]
        indexes = [
            models.Index(fields=["plan", "completed"]),
            models.Index(fields=["is_deleted"]),
        ]

    def __str__(self) -> str:
        return f"{self.plan.title}: {self.description[:50]}"


class RiskAction(AuditMixin, models.Model):
    risk_assessment = models.ForeignKey(
        "riesgos.RiskAssessment", on_delete=models.CASCADE, related_name="actions"
    )
    description = models.TextField()
    responsible = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True
    )
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    evidence = models.FileField(
        upload_to="risk_actions_evidence/", blank=True, null=True
    )
    comments = models.TextField(blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "risk_actions"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.risk_assessment}: {self.description[:40]}"
