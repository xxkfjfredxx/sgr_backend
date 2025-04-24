from django.db import models
from apps.empleados.models import Employee

class AccessLog(models.Model):
    ACCESS_TYPE_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    access_type = models.CharField(max_length=10, choices=ACCESS_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=30, blank=True, help_text="Método: manual, biometría, QR, etc.")
    remarks = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.get_access_type_display()} - {self.timestamp}"
   
class RiskAcceptanceForm(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task_description = models.TextField()
    risk_description = models.TextField()
    date = models.DateField(auto_now_add=True)
    signature = models.ImageField(upload_to='signatures/', null=True, blank=True)  # Aquí puedes guardar el "dibujo" de la firma o imagen de la huella
    accepted = models.BooleanField(default=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)  # Para registrar IP del dispositivo
    user_agent = models.TextField(blank=True, null=True)  # Para registrar info del dispositivo

    def __str__(self):
        return f"{self.employee} - {self.task_description[:30]} - {self.date}"