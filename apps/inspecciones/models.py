from django.db import models
from apps.empleados.models import Employee
from apps.usuarios.models import User

class InspectionTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class InspectionItem(models.Model):
    template = models.ForeignKey(InspectionTemplate, related_name='items', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.template.name}: {self.question[:50]}"

class Inspection(models.Model):
    template = models.ForeignKey(InspectionTemplate, on_delete=models.PROTECT)
    performed_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    location = models.CharField(max_length=150)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.template.name} - {self.location} ({self.date})"

class InspectionResponse(models.Model):
    inspection = models.ForeignKey(Inspection, related_name='responses', on_delete=models.CASCADE)
    item = models.ForeignKey(InspectionItem, on_delete=models.CASCADE)
    value = models.BooleanField()  # True: Cumple / False: No cumple
    observation = models.TextField(blank=True)
    evidence = models.FileField(upload_to='inspection_evidence/', blank=True, null=True)

    def __str__(self):
        return f"{self.inspection} - {self.item.question[:30]} - {'Sí' if self.value else 'No'}"
