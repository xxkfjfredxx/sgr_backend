from django.db import models
from apps.empleados.models import Employee

class WorkAccident(models.Model):
    INCIDENT_TYPE_CHOICES = [
        ('Accidente', 'Accidente de Trabajo'),
        ('Incidente', 'Incidente'),
    ]
    SEVERITY_CHOICES = [
        ("Leve", "Leve"),
        ("Grave", "Grave"),
        ("Mortal", "Mortal"),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    incident_type = models.CharField(
        max_length=20,
        choices=INCIDENT_TYPE_CHOICES,
        default='Accidente'  # <--- Aquí el default
    )
    date = models.DateField()
    location = models.CharField(max_length=150)
    description = models.TextField()
    injury_type = models.CharField(max_length=100, blank=True)
    severity = models.CharField(
        max_length=30,
        choices=SEVERITY_CHOICES,
        blank=True,
        default='Leve'  # <--- Aquí el default, puedes cambiarlo según tu criterio
    )
    reported_to_arl = models.BooleanField(default=False)
    days_lost = models.IntegerField(default=0, blank=True, null=True)
    training_valid = models.BooleanField(default=False, help_text="¿Tenía capacitación vigente?")
    medical_exam_valid = models.BooleanField(default=False, help_text="¿Tenía aptitud médica vigente?")
    corrective_actions = models.TextField(blank=True)
    evidence_file = models.FileField(upload_to='accident_evidence/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.incident_type} - {self.employee} - {self.date}"


class WorkAtHeightPermit(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=150)
    work_description = models.TextField()
    checklist = models.JSONField(default=dict, blank=True, help_text="Checklist de control de riesgos")
    approved = models.BooleanField(default=False)
    supervisor = models.CharField(max_length=100, blank=True)
    evidence_file = models.FileField(upload_to='height_permits/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Permiso Alturas: {self.employee} - {self.date} - {'Aprobado' if self.approved else 'Pendiente'}"
