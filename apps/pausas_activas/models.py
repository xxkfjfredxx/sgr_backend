from django.db import models

class ActivePauseSession(models.Model):
    date = models.DateField()
    topic = models.CharField(max_length=120, blank=True)  # Ej: "Estiramientos de cuello"
    facilitator = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.topic}"

class ActivePauseAttendance(models.Model):
    session = models.ForeignKey(ActivePauseSession, on_delete=models.CASCADE, related_name='attendances')
    employee = models.ForeignKey('empleados.Employee', on_delete=models.CASCADE)
    attended = models.BooleanField(default=True)
    signature = models.ImageField(upload_to='pausas_firmas/', blank=True, null=True)  # opcional: para firma digital

    class Meta:
        unique_together = ('session', 'employee')

    def __str__(self):
        return f"{self.employee} - {self.session} - {'Present' if self.attended else 'Absent'}"
