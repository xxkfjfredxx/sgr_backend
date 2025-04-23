from django.db import models

class Indicator(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    formula = models.TextField()
    unit = models.CharField(max_length=50)
    frequency = models.CharField(max_length=20, choices=[("Mensual", "Mensual"), ("Anual", "Anual")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class IndicatorResult(models.Model):  # <- ESTE DEBE EXISTIR
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    period = models.CharField(max_length=20)  # Ej: "2024-03"
    value = models.DecimalField(max_digits=10, decimal_places=2)
    interpretation = models.TextField(blank=True, null=True)
    generated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)