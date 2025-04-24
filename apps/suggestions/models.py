from django.db import models
from apps.empleados.models import Employee

class SuggestionBox(models.Model):
    SUGGESTION_TYPE_CHOICES = [
        ('Sugerencia', 'Sugerencia'),
        ('Queja', 'Queja'),
        ('Reporte', 'Reporte de Condición Insegura'),
        ('Mejora', 'Propuesta de Mejora'),
        ('Otro', 'Otro'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=30, choices=SUGGESTION_TYPE_CHOICES)
    title = models.CharField(max_length=150)
    description = models.TextField()
    anonymous = models.BooleanField(default=False)
    response = models.TextField(blank=True, help_text="Respuesta de la empresa/SST")
    responded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.type}: {self.title}"
