from django.db import models
from apps.empleados.models import Employee
from apps.empresa.models import Company
from apps.utils.mixins import AuditMixin

class AccessLog(AuditMixin, models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    ACCESS_TYPE_CHOICES = [
        ("ingreso", "Ingreso"),
        ("egreso", "Egreso"),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    access_type = models.CharField(max_length=10, choices=ACCESS_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    method = models.CharField(
        max_length=30, blank=True, help_text="manual, biometría, QR…"
    )
    remarks = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["-timestamp"]  # 👈 ya no tienes que usar .order_by() en la vista

    def __str__(self) -> str:
        return f"{self.employee} · {self.get_access_type_display()} · {self.timestamp}"
    

class RiskAcceptanceForm(AuditMixin, models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task_description = models.TextField()
    risk_description = models.TextField()
    date = models.DateField(auto_now_add=True)
    signature = models.ImageField(upload_to="signatures/", null=True, blank=True)
    accepted = models.BooleanField(default=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self) -> str:
        return f"{self.employee} · {self.task_description[:30]} · {self.date}"
