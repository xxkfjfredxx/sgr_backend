from django.db import models
from apps.core.models import TenantBase
from apps.utils.mixins import AuditMixin


class Area(AuditMixin, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    responsible = models.ForeignKey(
        "empleados.Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="areas_responsible",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Hazard(AuditMixin, models.Model):
    area = models.ForeignKey("Area", on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    source = models.CharField(max_length=100, blank=True)  # física, química, etc.
    risk_type = models.CharField(max_length=100, blank=True)  # cortante, inflamable…

    class Meta:
        ordering = ["area__name", "description"]

    def __str__(self):
        return f"{self.area} – {self.description}"


class RiskAssessment(TenantBase,AuditMixin, models.Model):
    hazard = models.ForeignKey("Hazard", on_delete=models.CASCADE, db_index=True)
    date = models.DateField(db_index=True)
    probability = models.IntegerField()
    severity = models.IntegerField()
    level = models.IntegerField()  # prob × sev → se sobrescribe en save()
    controls = models.TextField(blank=True)
    evaluated_by = models.ForeignKey(
        "empleados.Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="risk_evaluations",
    )
    review_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True, db_index=True)
    action_item = models.ForeignKey(
        "acciones_correctivas.ActionItem",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        db_table  = "risk_assessments"
        ordering  = ["-date"]
        indexes = [
            # Tenant filter + PK
            models.Index(fields=["company_id", "id"]),
            # Búsqueda por hazard y estado
            models.Index(fields=["hazard", "is_active"]),
            # Si tienes soft-delete
            models.Index(fields=["is_deleted"]),
        ]

    def __str__(self):
        return f"{self.hazard} ({self.date})"

    def save(self, *args, **kwargs):
        self.level = self.probability * self.severity
        super().save(*args, **kwargs)


class RiskControl(AuditMixin, models.Model):
    risk_assessment = models.ForeignKey(
        "RiskAssessment", on_delete=models.CASCADE, related_name="risk_controls"
    )
    description = models.TextField()
    implemented = models.BooleanField(default=False)
    responsible = models.ForeignKey(
        "empleados.Employee", on_delete=models.SET_NULL, null=True, blank=True
    )
    due_date = models.DateField()

    class Meta:
        ordering = ["-due_date"]

    def __str__(self):
        return f"Control – {self.risk_assessment}"


class ControlEvidence(models.Model):
    control = models.ForeignKey(
        "RiskControl", on_delete=models.CASCADE, related_name="evidences"
    )
    file = models.FileField(upload_to="control_evidences/")
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ControlFollowUp(models.Model):
    control = models.ForeignKey(
        "RiskControl", on_delete=models.CASCADE, related_name="followups"
    )
    date = models.DateField(auto_now_add=True)
    performed_by = models.ForeignKey(
        "empleados.Employee", on_delete=models.SET_NULL, null=True
    )
    notes = models.TextField(blank=True)
    is_controlled = models.BooleanField(default=False)


class RiskReview(AuditMixin, models.Model):
    risk_assessment = models.ForeignKey(
        "RiskAssessment", on_delete=models.CASCADE, related_name="reviews"
    )
    review_date = models.DateField()
    reviewed_by = models.ForeignKey(
        "empleados.Employee", on_delete=models.SET_NULL, null=True, blank=True
    )
    comments = models.TextField(blank=True)
    risk_level_after_review = models.IntegerField()

    class Meta:
        ordering = ["-review_date"]

    def __str__(self):
        return f"Review {self.risk_assessment} – {self.review_date}"
