from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    position = models.ForeignKey('catalogos.Position', on_delete=models.CASCADE, related_name='tasks')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position.name}"

class IPVRMatrix(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='ipvr')
    hazard = models.CharField(max_length=150)   # Peligro
    risk = models.CharField(max_length=150)     # Riesgo
    control = models.TextField()                # Medidas de control
    severity = models.CharField(max_length=50, blank=True)
    probability = models.CharField(max_length=50, blank=True)
    evaluation = models.CharField(max_length=50, blank=True)  # Bajo/Medio/Alto
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.name} - {self.hazard}"
