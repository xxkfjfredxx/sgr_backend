from django.db import models
from apps.empleados.models import Employee
from apps.utils.mixins import AuditMixin


class Reintegro(AuditMixin, models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(help_text="Inicio del proceso de reintegro")
    end_date = models.DateField(
        blank=True, null=True, help_text="Fin del proceso (si aplica)"
    )
    medical_recommendations = models.TextField(blank=True)
    position_modification = models.BooleanField(default=False)
    workplace_adaptation = models.BooleanField(default=False)
    observations = models.TextField(blank=True)
    successful = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"Reintegro {self.employee} – {self.start_date}"
