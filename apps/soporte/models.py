from django.db import models
from apps.usuarios.models import User

class SupportTicket(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    status = models.CharField(
        max_length=20,
        choices=[('open', 'Abierto'), ('in_progress', 'En Progreso'), ('closed', 'Cerrado')],
        default='open'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MaintenanceSchedule(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    scheduled_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    completed = models.BooleanField(default=False)

class MaintenanceRecord(models.Model):
    schedule = models.ForeignKey(MaintenanceSchedule, on_delete=models.CASCADE)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    performed_date = models.DateField()
    comments = models.TextField(blank=True)
