from django.db import models
from django.contrib.auth import get_user_model

class Activity(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En progreso'),
        ('completed', 'Finalizada'),
        ('cancelled', 'Cancelada'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Opcional para eventos de varios días
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
