from django.db import models
from apps.empleados.models import Employee
from apps.empresa.models import Company

class EmploymentLink(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    area = models.CharField(max_length=100, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='ACTIVE')

    class Meta:
        db_table = 'employment_links'

    def __str__(self):
        return f"{self.employee} - {self.company} ({self.status})"
