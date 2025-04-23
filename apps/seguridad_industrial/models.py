from django.db import models
from apps.empleados.models import Employee


class WorkAccident(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=150)
    description = models.TextField()
    injury_type = models.CharField(max_length=100)
    severity = models.CharField(max_length=30, choices=[("Leve", "Leve"), ("Grave", "Grave"), ("Mortal", "Mortal")])
    reported_to_arl = models.BooleanField(default=False)
    days_lost = models.IntegerField(default=0)
