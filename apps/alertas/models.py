from django.db import models
from apps.empleados.models import Employee

class DocumentAlert(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=100)  # Ej: "Curso Alturas", "Examen Médico"
    expiration_date = models.DateField()
    notified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)