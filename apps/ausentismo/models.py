from django.shortcuts import render
from django.db import models
from apps.empleados.models import Employee

class Absence(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    absence_type = models.CharField(max_length=30, choices=[("Incapacidad", "Incapacidad"), ("Licencia", "Licencia"), ("Vacaciones", "Vacaciones")])
    start_date = models.DateField()
    end_date = models.DateField()
    diagnosis_code = models.CharField(max_length=20, blank=True, null=True)
    diagnosis_description = models.CharField(max_length=255, blank=True, null=True)
    health_provider = models.CharField(max_length=100, blank=True, null=True)
    reintegrated = models.BooleanField(default=False)