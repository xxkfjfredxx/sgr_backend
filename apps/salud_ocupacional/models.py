from django.db import models
from apps.core.models import TenantBase
from apps.empleados.models import Employee
from apps.empresa.models import Company
from apps.utils.mixins import AuditMixin
from dateutil.relativedelta import relativedelta

try:
    # Para Django ≥ 3.1: JSONField funciona con MySQL/MariaDB y no necesita psycopg2
    from django.db.models import JSONField
except ImportError:
    # Fallback solo si realmente estuvieras en una versión antigua de Django y PostgreSQL
    from django.contrib.postgres.fields import JSONField


def document_upload_path(instance, filename):
    # (si tienes función de upload propia para exams)
    return f"medical-exams/{instance.employee.id}/{filename}"


class MedicalExam(TenantBase,AuditMixin, models.Model):
    """
    Exámenes médicos de SST: ingreso, periódico y retiro.
    Se registran resultados, entidad ejecutora, nivel de riesgo y próximos vencimientos.
    """

    # Fases del examen
    EXAM_PHASES = [
        ("Ingreso", "Ingreso"),
        ("Periódico", "Periódico"),
        ("Retiro", "Retiro"),
    ]
    # Lista de tipos de examen médico (reemplaza sub_type → exam_type)
    EXAM_TYPES = [
        ("Médico general", "Médico general"),
        ("Médico ocupacional", "Médico ocupacional"),
        (
            "Ingreso osteomuscular con énfasis en altura",
            "Ingreso osteomuscular con énfasis en altura",
        ),
        ("Laboratorio", "Laboratorio"),
        ("Visión", "Visión"),
        ("Auditivo", "Auditivo"),
        ("Espirometría", "Espirometría"),
        ("Electrocardiograma", "Electrocardiograma"),
        ("Radio de tórax", "Radio de tórax"),
        ("Psicológico", "Psicológico"),
        ("Psicotécnico", "Psicotécnico"),
        ("Osteomuscular", "Osteomuscular"),
        ("Pruebas de embarazo", "Pruebas de embarazo"),
        ("Específicas", "Específicas"),
    ]
    NEXT_DUE_CHOICES = [(i, f"{i} meses") for i in range(3, 25, 3)]  # 3 a 24 de 3 en 3
    exam_type = models.CharField(max_length=100, choices=EXAM_TYPES)

    # Campos del modelo
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    exam_phase = models.CharField(max_length=20, choices=EXAM_PHASES)
    date = models.DateField()
    entity_ips = models.CharField(max_length=100)
    aptitude = models.CharField(max_length=100)
    recommendations = models.TextField(blank=True)
    file = models.FileField(upload_to=document_upload_path, blank=True, null=True)
    next_due_months = models.IntegerField(
        choices=NEXT_DUE_CHOICES, blank=True, null=True
    )  # Nuevo campo

    # Resultados medidos y fecha de próximo examen
    metrics = JSONField(
        blank=True,
        null=True,
        help_text="Resultados específicos (p.ej. {'dB':25,'next_due':'2025-10-01'})",
    )
    next_due = models.DateField(
        blank=True, null=True, help_text="Fecha calculada para próximo examen"
    )

    class Meta:
        ordering = ["-date"]
        verbose_name = "Examen Médico"
        verbose_name_plural = "Exámenes Médicos"

    def save(self, *args, **kwargs):
        if self.date and self.next_due_months:
            self.next_due = self.date + relativedelta(months=self.next_due_months)
        else:
            self.next_due = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee} – {self.exam_phase}/{self.exam_type} – {self.date}"
