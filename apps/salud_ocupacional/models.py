from django.db import models
from apps.empleados.models import Employee
from apps.utils.mixins import AuditMixin


class MedicalExam(AuditMixin, models.Model):
    EXAM_CHOICES = [
        ("Ingreso",   "Ingreso"),
        ("Periódico", "Periódico"),
        ("Retiro",    "Retiro"),
    ]

    employee        = models.ForeignKey(Employee, on_delete=models.CASCADE)
    exam_type       = models.CharField(max_length=20, choices=EXAM_CHOICES)
    date            = models.DateField()
    entity          = models.CharField(max_length=100)
    aptitude        = models.CharField(max_length=100)
    recommendations = models.TextField(blank=True)
    file            = models.FileField(upload_to="medical-exams/", blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.employee} – {self.exam_type} – {self.date}"
