from django.db import models
from apps.utils.mixins import AuditMixin


class Indicator(AuditMixin, models.Model):
    FREQUENCY_CHOICES = [("Mensual", "Mensual"), ("Anual", "Anual")]

    name        = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    formula     = models.TextField()
    unit        = models.CharField(max_length=50)
    frequency   = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class IndicatorResult(AuditMixin, models.Model):
    indicator      = models.ForeignKey(Indicator, on_delete=models.CASCADE, related_name="results")
    period         = models.CharField(max_length=20)           # ej. “2025-03”
    value          = models.DecimalField(max_digits=12, decimal_places=2)
    interpretation = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-period"]
        unique_together = ("indicator", "period")

    def __str__(self):
        return f"{self.indicator} – {self.period}: {self.value}{self.indicator.unit}"
