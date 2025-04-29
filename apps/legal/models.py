from django.db import models
from apps.catalogos.models import WorkArea
from apps.utils.mixins import AuditMixin


class LegalRequirement(AuditMixin, models.Model):
    name            = models.CharField(max_length=200)
    description     = models.TextField()
    area            = models.ForeignKey(WorkArea, on_delete=models.SET_NULL, null=True, blank=True,
                                        help_text="Área o proceso relacionado")
    law_reference   = models.CharField(max_length=200, blank=True, help_text="Ley / Norma / Decreto / Contrato")
    document        = models.FileField(upload_to="legal_requirements/", blank=True, null=True)
    effective_date  = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    reviewed_by     = models.CharField(max_length=100, blank=True)
    review_date     = models.DateField(blank=True, null=True)
    comments        = models.TextField(blank=True)
    active          = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
