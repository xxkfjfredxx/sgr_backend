from django.db import models
from apps.empleados.models import Employee
from apps.empresa.models import Company
from apps.contratistas.models import ContractorCompany
from apps.utils.mixins import AuditMixin


class Contract(AuditMixin, models.Model):
    CONTRACT_TYPE_CHOICES = [
        ("Laboral", "Laboral"),
        ("Servicios", "Servicios"),
        ("Aprendizaje", "Aprendizaje"),
        ("Temporal", "Temporal"),
        ("Otro", "Otro"),
    ]
    STATUS_CHOICES = [
        ("VIGENTE", "Vigente"),
        ("TERMINADO", "Terminado"),
        ("LIQUIDADO", "Liquidado"),
        ("SUSPENDIDO", "Suspendido"),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="contracts",
        null=True,
        blank=True,
    )
    contractor = models.ForeignKey(
        ContractorCompany, on_delete=models.SET_NULL, null=True, blank=True
    )
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True
    )
    contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    renewal_count = models.IntegerField(default=0)
    contract_file = models.FileField(upload_to="contracts/", blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="VIGENTE")
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        who = self.employee or self.contractor
        return f"{who} – {self.contract_type} ({self.status})"
