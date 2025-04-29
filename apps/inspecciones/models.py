from django.db import models
from apps.empleados.models import Employee
from apps.utils.mixins import AuditMixin


class InspectionTemplate(AuditMixin, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class InspectionItem(AuditMixin, models.Model):
    template = models.ForeignKey(
        InspectionTemplate, related_name="items", on_delete=models.CASCADE
    )
    question = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.template} – {self.question[:50]}"


class Inspection(AuditMixin, models.Model):
    template = models.ForeignKey(InspectionTemplate, on_delete=models.PROTECT)
    performed_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateField()
    location = models.CharField(max_length=150)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.template} – {self.location} ({self.date})"


class InspectionResponse(AuditMixin, models.Model):
    inspection = models.ForeignKey(
        Inspection, related_name="responses", on_delete=models.CASCADE
    )
    item = models.ForeignKey(InspectionItem, on_delete=models.CASCADE)
    value = models.BooleanField()  # True = cumple
    observation = models.TextField(blank=True)
    evidence = models.FileField(upload_to="inspection_evidence/", blank=True, null=True)

    class Meta:
        ordering = ["item_id"]

    def __str__(self):
        return f"{self.inspection} – {self.item.question[:30]} – {'Sí' if self.value else 'No'}"
