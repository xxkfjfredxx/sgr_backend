from django.db import models
from apps.empleados.models import Employee

class Reintegro(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(help_text="Fecha inicio del proceso de reintegro")
    end_date = models.DateField(blank=True, null=True, help_text="Fecha de finalización (si aplica)")
    medical_recommendations = models.TextField(blank=True, help_text="Recomendaciones médicas para el reintegro")
    position_modification = models.BooleanField(default=False, help_text="¿Hubo modificación de cargo?")
    workplace_adaptation = models.BooleanField(default=False, help_text="¿Hubo adaptación en el puesto de trabajo?")
    observations = models.TextField(blank=True)
    successful = models.BooleanField(default=False, help_text="¿Reintegro exitoso?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reintegro de {self.employee} - {self.start_date}"
