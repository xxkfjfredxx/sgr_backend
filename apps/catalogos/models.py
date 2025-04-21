from django.db import models

class Branch(models.Model):  # Sucursal
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'branches'

    def __str__(self):
        return self.name


class Position(models.Model):  # Cargo
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'positions'

    def __str__(self):
        return self.name


class WorkArea(models.Model):  # Área
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'work_areas'

    def __str__(self):
        return self.name
    
    
class DocumentType(models.Model):  # Tipo de Documento
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'document_types'

    def __str__(self):
        return self.name
