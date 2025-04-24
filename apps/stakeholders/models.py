from django.db import models
from apps.catalogos.models import WorkArea  # O el modelo que manejes para áreas

class Stakeholder(models.Model):
    STAKEHOLDER_TYPE_CHOICES = [
        ('Cliente', 'Cliente'),
        ('Proveedor', 'Proveedor'),
        ('Contratista', 'Contratista'),
        ('ARL', 'ARL'),
        ('Aseguradora', 'Aseguradora'),
        ('Autoridad', 'Autoridad Reguladora'),
        ('Comunidad', 'Comunidad'),
        ('Otro', 'Otro'),
    ]
    name = models.CharField(max_length=150)
    stakeholder_type = models.CharField(max_length=30, choices=STAKEHOLDER_TYPE_CHOICES)
    contact_info = models.CharField(max_length=250, blank=True)
    interests = models.TextField(help_text="Expectativas o intereses sobre el SG-SST")
    requirements = models.TextField(blank=True, help_text="Requisitos legales, contractuales, etc.")
    work_area = models.ForeignKey(WorkArea, on_delete=models.SET_NULL, null=True, blank=True, help_text="Área/proceso asociado")
    document = models.FileField(upload_to='stakeholder_docs/', blank=True, null=True, help_text="Documento asociado")
    last_contact = models.DateField(null=True, blank=True, help_text="Último contacto/actualización")
    comments = models.TextField(blank=True, help_text="Observaciones internas")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Para control de cambios

    def __str__(self):
        return f"{self.name} ({self.stakeholder_type})"
