from django.db import models
from apps.usuarios.models import User

class SSTObjective(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='objectives')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En progreso'),
        ('completed', 'Cumplido'),
        ('overdue', 'Vencido'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title

class SSTGoal(models.Model):
    objective = models.ForeignKey(SSTObjective, on_delete=models.CASCADE, related_name='goals')
    description = models.CharField(max_length=255)
    indicator = models.CharField(max_length=100, blank=True, help_text="Ej: % accidentes reducidos")
    target_value = models.CharField(max_length=100, blank=True, help_text="Ej: 10% menos accidentes")
    evidence_file = models.FileField(upload_to='sst_goals/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=SSTObjective.STATUS_CHOICES, default='pending')
    comment = models.TextField(blank=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.objective.title} - {self.description}"
