from apps.empleados.models import Employee
from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='areas_responsible')

    def __str__(self):
        return self.name

class Hazard(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    source = models.CharField(max_length=100, blank=True)  # Fuente: química, física, biológica, etc.
    risk_type = models.CharField(max_length=100, blank=True)  # Tipo: cortante, inflamable, etc.

    def __str__(self):
        return f"{self.area.name} - {self.description}"

class RiskAssessment(models.Model):
    hazard = models.ForeignKey(Hazard, on_delete=models.CASCADE)
    date = models.DateField()
    probability = models.IntegerField()  # Ej: 1-5
    severity = models.IntegerField()     # Ej: 1-5
    level = models.IntegerField()        # Calculado: probabilidad x severidad
    controls = models.TextField(blank=True)
    evaluated_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='risk_evaluations')
    review_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hazard} ({self.date})"

    def save(self, *args, **kwargs):
        self.level = self.probability * self.severity
        super().save(*args, **kwargs)
