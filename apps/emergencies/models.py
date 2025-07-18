from django.db import models
 
from apps.empleados.models import Employee
from apps.empresa.models import Company
from apps.utils.mixins import AuditMixin


class EmergencyBrigadeMember(AuditMixin, models.Model):
    ROLE_CHOICES = [
        ("Jefe", "Jefe de Brigada"),
        ("PrimerosAuxilios", "Primeros Auxilios"),
        ("Evacuacion", "Evacuación"),
        ("Incendios", "Control de Incendios"),
        ("Comunicaciones", "Comunicaciones"),
        ("Otro", "Otro"),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "emergency_brigade_member"
        ordering = ["employee__first_name"]

    def __str__(self):
        return f"{self.employee} – {self.role}"


class EmergencyEquipment(AuditMixin, models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    EQUIPMENT_TYPE_CHOICES = [
        ("Extintor", "Extintor"),
        ("Botiquin", "Botiquín"),
        ("Alarma", "Alarma"),
        ("Camilla", "Camilla"),
        ("Otro", "Otro"),
    ]
    type = models.CharField(max_length=50, choices=EQUIPMENT_TYPE_CHOICES)
    location = models.CharField(max_length=100)
    inspection_date = models.DateField(null=True, blank=True)
    next_inspection = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = "emergency_equipment"
        ordering = ["type", "location"]

    def __str__(self):
        return f"{self.type} – {self.location}"


class EmergencyDrill(AuditMixin, models.Model):
    DRILL_TYPE_CHOICES = [
        ("Evacuacion", "Evacuación"),
        ("Incendio", "Incendio"),
        ("Sismo", "Sismo"),
        ("PrimerosAuxilios", "Primeros Auxilios"),
        ("Otro", "Otro"),
    ]
    drill_type = models.CharField(max_length=50, choices=DRILL_TYPE_CHOICES)
    date = models.DateField()
    objectives = models.TextField()
    participants = models.ManyToManyField(Employee, related_name="drill_participations")
    findings = models.TextField(blank=True)
    improvement_actions = models.TextField(blank=True)
    evidence_file = models.FileField(
        upload_to="emergency_drills/", blank=True, null=True
    )

    class Meta:
        db_table = "emergency_drill"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.drill_type} – {self.date}"
