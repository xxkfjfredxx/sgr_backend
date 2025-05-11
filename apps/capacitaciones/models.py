from django.db import models
from apps.empleados.models import Employee
from apps.utils.mixins import AuditMixin
from apps.empresa.models import Company
from django.db.models import Q, UniqueConstraint


class TrainingSession(AuditMixin, models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    duration_hours = models.PositiveSmallIntegerField(null=True, blank=True)
    modality = models.CharField(max_length=20, blank=True)
    topic = models.CharField(max_length=150)
    date = models.DateField()
    instructor = models.CharField(max_length=100)
    supporting_document = models.FileField(
        upload_to="training-sessions/", blank=True, null=True
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.topic} – {self.date}"


class TrainingSessionAttendance(AuditMixin, models.Model):
    session = models.ForeignKey(
        TrainingSession, on_delete=models.CASCADE, related_name="attendances"
    )
    signature_file = models.FileField(upload_to="attendances/", blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attended = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]
        # ⬇️  NUEVA restricción: aplica solo cuando is_deleted = False
        constraints = [
            UniqueConstraint(
                fields=["session", "employee"],
                condition=Q(is_deleted=False),
                name="unique_attendance_active",
            )
        ]

    def __str__(self):
        return f"{self.employee} – {self.session.topic}"


class Certification(AuditMixin, models.Model):
    participant = models.ForeignKey(
        TrainingSessionAttendance,
        on_delete=models.CASCADE,
        related_name="certifications",
    )
    certificate_file = models.FileField(upload_to="certifications/")
    issued_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-issued_date"]

    def __str__(self):
        return f"Certificación {self.participant.employee} – {self.participant.session.topic}"
