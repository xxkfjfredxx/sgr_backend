from django.db import models
from django.conf import settings
import os
from datetime import datetime


class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    document = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    eps = models.CharField(max_length=100, blank=True, null=True)
    afp = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    phone_contact = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    ethnicity = models.CharField(max_length=50, blank=True, null=True)
    socioeconomic_stratum = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.name


def document_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    doc_type = instance.document_type.name.lower().replace(' ', '_')
    date_path = datetime.now().strftime('%Y/%m/%d')
    filename = f"{doc_type}-emp{instance.employee.id}-{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    print("DEBUG -> DocumentType ID:", instance.document_type.id)
    print("DEBUG -> DocumentType Name:", instance.document_type.name)
    return os.path.join('documents', doc_type, date_path, filename)


class EmployeeDocument(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='documents')
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
    file = models.FileField(upload_to=document_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.document_type}"
