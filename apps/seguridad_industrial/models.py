from django.db import models
from apps.empleados.models import Employee
from apps.utils.mixins import AuditMixin


class WorkAccident(AuditMixin, models.Model):
    INCIDENT_CHOICES = [("Accidente", "Accidente de Trabajo"), ("Incidente", "Incidente")]
    SEVERITY_CHOICES = [("Leve", "Leve"), ("Grave", "Grave"), ("Mortal", "Mortal")]

    employee            = models.ForeignKey(Employee, on_delete=models.CASCADE)
    incident_type       = models.CharField(max_length=20, choices=INCIDENT_CHOICES, default="Accidente")
    date                = models.DateField()
    location            = models.CharField(max_length=150)
    description         = models.TextField()
    injury_type         = models.CharField(max_length=100, blank=True)
    severity            = models.CharField(max_length=30, choices=SEVERITY_CHOICES, default="Leve", blank=True)
    reported_to_arl     = models.BooleanField(default=False)
    days_lost           = models.IntegerField(default=0, blank=True, null=True)
    training_valid      = models.BooleanField(default=False)
    medical_exam_valid  = models.BooleanField(default=False)
    corrective_actions  = models.TextField(blank=True)
    evidence_file       = models.FileField(upload_to="accident_evidence/", blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.incident_type} – {self.employee} – {self.date}"


class WorkAtHeightPermit(AuditMixin, models.Model):
    employee          = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date              = models.DateField()
    location          = models.CharField(max_length=150)
    work_description  = models.TextField()
    checklist         = models.JSONField(default=dict, blank=True)
    approved          = models.BooleanField(default=False)
    supervisor        = models.CharField(max_length=100, blank=True)
    evidence_file     = models.FileField(upload_to="height_permits/", blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        state = "Aprobado" if self.approved else "Pendiente"
        return f"Permiso – {self.employee} – {self.date} – {state}"
