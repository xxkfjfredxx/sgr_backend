from django.db import models
from apps.empleados.models import Employee
from apps.utils.mixins import AuditMixin


class TrainingSession(AuditMixin, models.Model):
    topic                = models.CharField(max_length=150)
    date                 = models.DateField()
    instructor           = models.CharField(max_length=100)
    supporting_document  = models.FileField(upload_to="training-sessions/", blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.topic} – {self.date}"


class TrainingSessionAttendance(AuditMixin, models.Model):
    session   = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, related_name="attendances")
    employee  = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attended  = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("session", "employee")   # un empleado solo una asistencia por sesión

    def __str__(self):
        return f"{self.employee} – {self.session.topic}"


class Certification(AuditMixin, models.Model):
    participant       = models.ForeignKey(TrainingSessionAttendance, on_delete=models.CASCADE, related_name="certifications")
    certificate_file  = models.FileField(upload_to="certifications/")
    issued_date       = models.DateField(auto_now_add=True)
    expiration_date   = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-issued_date"]

    def __str__(self):
        return f"Certificación {self.participant.employee} – {self.participant.session.topic}"
