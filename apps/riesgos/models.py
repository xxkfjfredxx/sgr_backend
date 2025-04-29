# apps/riesgos/models.py
from django.db import models
from apps.utils.mixins import AuditMixin

# ──────────────────── MODELOS PRINCIPALES ────────────────────

class Area(AuditMixin, models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    responsible = models.ForeignKey(
        "empleados.Employee",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="areas_responsible"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Hazard(AuditMixin, models.Model):
    area        = models.ForeignKey("Area", on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    source      = models.CharField(max_length=100, blank=True)   # física, química, etc.
    risk_type   = models.CharField(max_length=100, blank=True)   # cortante, inflamable…

    class Meta:
        ordering = ["area__name", "description"]

    def __str__(self):
        return f"{self.area} – {self.description}"


class RiskAssessment(AuditMixin, models.Model):
    hazard        = models.ForeignKey("Hazard", on_delete=models.CASCADE)
    date          = models.DateField()
    probability   = models.IntegerField()
    severity      = models.IntegerField()
    level         = models.IntegerField()  # prob × sev → se sobrescribe en save()
    controls      = models.TextField(blank=True)
    evaluated_by  = models.ForeignKey(
        "empleados.Employee", on_delete=models.SET_NULL,
        null=True, blank=True, related_name="risk_evaluations"
    )
    review_date   = models.DateField(null=True, blank=True)
    is_active     = models.BooleanField(default=True)
    action_item   = models.ForeignKey(
        "acciones_correctivas.ActionItem",
        on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        ordering = ["-date"]

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


class RiskReview(AuditMixin, models.Model):
    risk_assessment = models.ForeignKey(
        "RiskAssessment", on_delete=models.CASCADE, related_name="reviews"
    )
    review_date            = models.DateField()
    reviewed_by            = models.ForeignKey(
        "empleados.Employee", on_delete=models.SET_NULL, null=True, blank=True
    )
    comments               = models.TextField(blank=True)
    risk_level_after_review = models.IntegerField()

    class Meta:
        ordering = ["-review_date"]

    def __str__(self):
        return f"Review {self.risk_assessment} – {self.review_date}"
