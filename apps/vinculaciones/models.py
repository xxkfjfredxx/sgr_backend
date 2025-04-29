from django.db import models
from apps.utils.mixins import AuditMixin
from apps.empleados.models import Employee
from apps.empresa.models import Company


class EmploymentLink(AuditMixin, models.Model):
    STATUS_CHOICES = [
        ("ACTIVE", "Activo"),
        ("INACTIVE", "Inactivo"),
        ("ENDED", "Finalizado"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_index=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, db_index=True)

    position = models.CharField(max_length=100)
    area = models.CharField(max_length=100, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    start_date = models.DateField(db_index=True)
    end_date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="ACTIVE",
        db_index=True,
    )

    class Meta:
        db_table = "employment_links"
        ordering = ["-start_date"]
        indexes = [
            models.Index(fields=["company", "status"]),
            models.Index(fields=["is_deleted"]),
        ]

    def __str__(self):
        return f"{self.employee} – {self.company} ({self.status})"
