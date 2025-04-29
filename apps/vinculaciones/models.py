from django.db import models
from apps.utils.mixins import AuditMixin
from apps.empleados.models import Employee
from apps.empresa.models import Company


class EmploymentLink(AuditMixin, models.Model):
    STATUS_CHOICES = [
        ("ACTIVE",   "Activo"),
        ("INACTIVE", "Inactivo"),
        ("ENDED",    "Finalizado"),
    ]

    employee   = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company    = models.ForeignKey(Company,  on_delete=models.CASCADE)
    position   = models.CharField(max_length=100)
    area       = models.CharField(max_length=100, blank=True, null=True)
    salary     = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date   = models.DateField(blank=True, null=True)
    status     = models.CharField(max_length=50, choices=STATUS_CHOICES, default="ACTIVE")

    class Meta:
        db_table  = "employment_links"
        ordering  = ["-start_date"]

    def __str__(self):
        return f"{self.employee} – {self.company} ({self.status})"
