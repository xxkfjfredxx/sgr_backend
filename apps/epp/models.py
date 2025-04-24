from django.db import models
from apps.empleados.models import Employee

class EPPItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=0)
    expiration_date = models.DateField(null=True, blank=True)  # Para control de vencimiento

    def __str__(self):
        return self.name

class EPPAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    epp_item = models.ForeignKey(EPPItem, on_delete=models.CASCADE)
    assigned_at = models.DateField(auto_now_add=True)
    returned_at = models.DateField(null=True, blank=True)
    condition_on_return = models.TextField(blank=True)
    assigned_by = models.CharField(max_length=100, blank=True)
    evidence = models.FileField(upload_to='epp_evidence/', blank=True, null=True)
    is_active = models.BooleanField(default=True)  # True si el EPP aún está en poder del empleado

    def __str__(self):
        return f"{self.employee} - {self.epp_item} ({'Activo' if self.is_active else 'Devuelto'})"
