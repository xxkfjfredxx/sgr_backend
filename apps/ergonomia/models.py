from django.db import models
from apps.utils.mixins import AuditMixin


class ErgonomicAssessment(AuditMixin, models.Model):
    employee = models.ForeignKey(
        "empleados.Employee",
        on_delete=models.CASCADE,
        related_name="ergonomic_assessments",
    )
    position = models.ForeignKey(
        "catalogos.Position", on_delete=models.SET_NULL, null=True, blank=True
    )
    area = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    evaluation_type = models.CharField(
        max_length=100, blank=True
    )  # Ej.: Postural, Manual handling
    summary = models.TextField(blank=True)
    file = models.FileField(upload_to="ergonomics/", blank=True, null=True)
    responsible = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "ergonomic_assessment"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.employee} – {self.date} – {self.evaluation_type}"


class ARO(AuditMixin, models.Model):
    employee = models.ForeignKey(
        "empleados.Employee", on_delete=models.SET_NULL, null=True, blank=True
    )
    position = models.ForeignKey(
        "catalogos.Position", on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateField()
    description = models.TextField()
    hazard = models.CharField(max_length=150)
    risk = models.CharField(max_length=150)
    control = models.TextField()
    evidence = models.FileField(upload_to="aro/", blank=True, null=True)

    class Meta:
        db_table = "aro"
        ordering = ["-date"]

    def __str__(self):
        return f"ARO: {self.hazard} ({self.date})"


class ATS(AuditMixin, models.Model):
    employee = models.ForeignKey(
        "empleados.Employee", on_delete=models.SET_NULL, null=True, blank=True
    )
    position = models.ForeignKey(
        "catalogos.Position", on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateField()
    activity = models.CharField(max_length=150)
    hazard = models.CharField(max_length=150)
    risk = models.CharField(max_length=150)
    control = models.TextField()
    evidence = models.FileField(upload_to="ats/", blank=True, null=True)

    class Meta:
        db_table = "ats"
        ordering = ["-date"]

    def __str__(self):
        return f"ATS: {self.activity} ({self.date})"
