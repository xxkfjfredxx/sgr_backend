from django.db import models
from apps.empleados.models import Employee

class MedicalExam(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=20, choices=[("Ingreso", "Ingreso"), ("Periódico", "Periódico"), ("Retiro", "Retiro")])
    date = models.DateField()
    entity = models.CharField(max_length=100)
    aptitude = models.CharField(max_length=100)
    recommendations = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='medical-exams/', blank=True, null=True)