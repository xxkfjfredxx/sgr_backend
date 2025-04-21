from django.db import models
from apps.empleados.models import Employee
from apps.usuarios.models import User  # quien subió el documento
from apps.catalogos.models import DocumentType
 # si ya lo migraste a otra app

class PersonalDocument(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    document_type = models.ForeignKey(DocumentType, on_delete=models.RESTRICT)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'personal_documents'

    def __str__(self):
        return self.file_name

