from django.db import models
from apps.empresa.models import Company
from apps.utils.mixins import AuditMixin


class EPPItem(AuditMixin, models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=0)
    expiration_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "epp_items"
        ordering = ["name"]

    def __str__(self):
        return self.name


class EPPAssignment(AuditMixin, models.Model):
    RETURN_REASON_CHOICES = [
        ("Desgaste", "Desgaste"),
        ("Daño", "Daño"),
        ("Vencimiento", "Vencimiento"),
        ("Pérdida", "Pérdida"),
        ("Reposición programada", "Reposición programada"),
    ]

    employee = models.ForeignKey("empleados.Employee", on_delete=models.CASCADE)
    epp_item = models.ForeignKey(EPPItem, on_delete=models.CASCADE)
    assigned_at = models.DateField(auto_now_add=True)
    returned_at = models.DateField(null=True, blank=True)
    condition_on_return = models.TextField(blank=True)
    assigned_by = models.CharField(max_length=100, blank=True)
    evidence = models.FileField(upload_to="epp_evidence/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    return_reason = models.CharField(
        max_length=30, choices=RETURN_REASON_CHOICES, blank=True
    )
    confirmed = models.BooleanField(default=False)
    confirmation_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "epp_assignments"
        ordering = ["-assigned_at"]

    def __str__(self):
        status = "Activo" if self.is_active else "Devuelto"
        return f"{self.employee} – {self.epp_item} ({status})"
