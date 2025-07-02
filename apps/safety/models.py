from django.db import models
from apps.core.models import TenantBase
from apps.empresa.models import Company
from apps.empleados.models import Employee


class SignageInventory(TenantBase,models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="signage_inventory"
    )
    tipo_senal = models.CharField("Tipo de señal", max_length=100)
    ubicacion_plano = models.JSONField("Ubicación (geoJSON)")
    photo = models.FileField(
        "Evidencia (foto)", upload_to="signage_inventory/", blank=True, null=True
    )
    installed_at = models.DateTimeField("Fecha de verificación", auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} – {self.tipo_senal}"


class VaccinationRecord(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="vaccinations"
    )
    vacuna = models.CharField("Vacuna", max_length=100)
    fecha = models.DateField("Fecha de aplicación")
    fecha_vencimiento = models.DateField("Fecha de vencimiento")
    soporte = models.FileField(
        "Soporte (PDF/foto)", upload_to="vaccination_records/", blank=True, null=True
    )

    def __str__(self):
        # Ajusta si tu Employee no tiene full_name
        return f"{self.employee.first_name} {self.employee.last_name} – {self.vacuna} ({self.fecha})"
