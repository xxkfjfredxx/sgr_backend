from django.db import models
from apps.empleados.models import Employee
from apps.empresa.models import Company
from apps.utils.mixins import AuditMixin

try:
    # Para Django ≥ 3.1: JSONField funciona con MySQL/MariaDB y no necesita psycopg2
    from django.db.models import JSONField
except ImportError:
    # Fallback solo si realmente estuvieras en una versión antigua de Django y PostgreSQL
    from django.contrib.postgres.fields import JSONField


def document_upload_path(instance, filename):
    # (si tienes función de upload propia para exams)
    return f"medical-exams/{instance.employee.id}/{filename}"


class MedicalExam(AuditMixin, models.Model):
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
    # Nivel de riesgo SST del puesto (I–IV)
    RISK_LEVELS = [
        ("I", "Bajo"),
        ("II", "Medio"),
        ("III", "Alto"),
        ("IV", "Crítico"),
    ]
    # Sub-tipo específico de examen
    SUB_TYPES = [
        ("Audiometría", "Audiometría"),
        ("Espirometría", "Espirometría"),
        ("Visión", "Visión"),
        ("Laboratorio", "Laboratorio"),
        ("Presión arterial", "Presión arterial"),
        ("Otro", "Otro"),
    ]

    # Campos del modelo
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    exam_phase = models.CharField(max_length=20, choices=EXAM_PHASES)
    sub_type = models.CharField(max_length=50, choices=SUB_TYPES, default="Otro")
    risk_level = models.CharField(
        max_length=5,
        choices=RISK_LEVELS,
        default="II",
        help_text="Nivel de riesgo SST del puesto",
    )
    date = models.DateField()
    entity = models.CharField(max_length=100)
    aptitude = models.CharField(max_length=100)
    recommendations = models.TextField(blank=True)
    file = models.FileField(upload_to=document_upload_path, blank=True, null=True)

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

    def __str__(self):
        return f"{self.employee} – {self.exam_phase}/{self.sub_type} – {self.date}"
