from django.db import models
from apps.empresa.models import Company


class EquipmentInventory(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="equipment_inventory"
    )
    categoria = models.CharField("Categoría", max_length=100)
    serial = models.CharField("Serial", max_length=100, blank=True, null=True)
    cantidad = models.PositiveIntegerField("Cantidad", default=1)
    fecha_compra = models.DateField("Fecha de compra")
    certificado = models.FileField(
        "Certificado", upload_to="equipment_certificates/", blank=True, null=True
    )
    estado = models.CharField("Estado", max_length=50, blank=True)

    class Meta:
        db_table = "equipment_inventory"
        ordering = ["categoria", "serial"]

    def __str__(self):
        if self.cantidad > 1:
            return f"{self.cantidad}× {self.categoria}"
        return f"{self.categoria} ({self.serial})"


class EquipmentInspection(models.Model):
    equipment = models.ForeignKey(
        EquipmentInventory,
        on_delete=models.CASCADE,
        related_name="inspections",
    )
    fecha = models.DateField("Fecha de inspección")
    resultado = models.CharField("Resultado", max_length=100)
    tecnico = models.CharField("Técnico", max_length=100)
    evidencia = models.FileField(
        "Evidencia (PDF/imagen)",
        upload_to="equipment_inspections/",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "equipment_inspections"
        ordering = ["-fecha"]

    def __str__(self):
        return f"Inspección {self.equipment.serial} – {self.fecha}"
