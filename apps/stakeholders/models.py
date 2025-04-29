from django.db import models
from apps.utils.mixins import AuditMixin
from apps.catalogos.models import WorkArea


class Stakeholder(AuditMixin, models.Model):
    TYPE_CHOICES = [
        ("Cliente",      "Cliente"),
        ("Proveedor",    "Proveedor"),
        ("Contratista",  "Contratista"),
        ("ARL",          "ARL"),
        ("Aseguradora",  "Aseguradora"),
        ("Autoridad",    "Autoridad Reguladora"),
        ("Comunidad",    "Comunidad"),
        ("Otro",         "Otro"),
    ]

    name          = models.CharField(max_length=150)
    stakeholder_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    contact_info  = models.CharField(max_length=250, blank=True)
    interests     = models.TextField()
    requirements  = models.TextField(blank=True)
    work_area     = models.ForeignKey(WorkArea, on_delete=models.SET_NULL, null=True, blank=True)
    document      = models.FileField(upload_to="stakeholder_docs/", blank=True, null=True)
    last_contact  = models.DateField(null=True, blank=True)
    comments      = models.TextField(blank=True)
    active        = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.stakeholder_type})"
