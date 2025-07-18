from django.db import models
from apps.empleados.models import Employee
from apps.utils.mixins import AuditMixin


class DocumentAlert(AuditMixin, models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=100)
    expiration_date = models.DateField()
    notified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    class Meta:
        db_table = "document_alerts"
        ordering = ["expiration_date"]  # ← ahora la vista no necesita .order_by()

    def __str__(self) -> str:
        return f"{self.employee} · {self.alert_type} → {self.expiration_date}"
