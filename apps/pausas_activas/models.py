from django.db import models
 
from apps.empresa.models import Company
from apps.utils.mixins import AuditMixin


class ActivePauseSession(AuditMixin, models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    topic = models.CharField(
        max_length=120, blank=True
    )  # Ej.: “Estiramientos de cuello”
    facilitator = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        db_table = "pausas_activas_session"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date} – {self.topic}"


class ActivePauseAttendance(AuditMixin, models.Model):
    session = models.ForeignKey(
        ActivePauseSession, on_delete=models.CASCADE, related_name="attendances"
    )
    employee = models.ForeignKey("empleados.Employee", on_delete=models.CASCADE)
    attended = models.BooleanField(default=True)
    signature = models.ImageField(upload_to="pausas_firmas/", blank=True, null=True)

    class Meta:
        db_table = "pausas_activas_attendance"
        unique_together = ("session", "employee")
        ordering = ["employee_id"]

    def __str__(self):
        state = "Presente" if self.attended else "Ausente"
        return f"{self.employee} – {self.session.date} – {state}"
