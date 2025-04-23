from django.db import models
from apps.empleados.models import Employee

class TrainingSession(models.Model):
    topic = models.CharField(max_length=150)
    date = models.DateField()
    instructor = models.CharField(max_length=100)
    supporting_document = models.FileField(upload_to='training-sessions/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TrainingSessionAttendance(models.Model):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attended = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)