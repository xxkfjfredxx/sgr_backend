from django.db import models
from apps.utils.mixins import AuditMixin


class Task(AuditMixin, models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    position = models.ForeignKey(
        "catalogos.Position", on_delete=models.CASCADE, related_name="tasks"
    )
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "tasks"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} – {self.position.name}"


class IPVRMatrix(AuditMixin, models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="ipvr")
    hazard = models.CharField(max_length=150)  # Peligro
    risk = models.CharField(max_length=150)  # Riesgo
    control = models.TextField()  # Medidas de control
    severity = models.CharField(max_length=50, blank=True)
    probability = models.CharField(max_length=50, blank=True)
    evaluation = models.CharField(max_length=50, blank=True)  # Bajo / Medio / Alto

    class Meta:
        db_table = "ipvr_matrix"
        ordering = ["task__name", "hazard"]

    def __str__(self):
        return f"{self.task.name} – {self.hazard}"
