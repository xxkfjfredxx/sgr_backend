from django.db import models
from apps.empleados.models import Employee
from apps.utils.mixins import AuditMixin


class Absence(AuditMixin, models.Model):
    ABSENCE_CHOICES = [
        ("Incapacidad", "Incapacidad"),
        ("Licencia", "Licencia"),
        ("Vacaciones", "Vacaciones"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    absence_type = models.CharField(max_length=30, choices=ABSENCE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    diagnosis_code = models.CharField(max_length=20, blank=True, null=True)
    diagnosis_description = models.CharField(max_length=255, blank=True, null=True)
    health_provider = models.CharField(max_length=100, blank=True, null=True)
    reintegrated = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self) -> str:
        return (
            f"{self.employee} · {self.absence_type} ({self.start_date}→{self.end_date})"
        )
