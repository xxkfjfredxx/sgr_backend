from apps.empleados.models import Employee
from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='areas_responsible')

    def __str__(self):
        return self.name

class Hazard(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    source = models.CharField(max_length=100, blank=True)  # Fuente: química, física, biológica, etc.
    risk_type = models.CharField(max_length=100, blank=True)  # Tipo: cortante, inflamable, etc.

    def __str__(self):
        return f"{self.area.name} - {self.description}"

class RiskAssessment(models.Model):
    hazard = models.ForeignKey(Hazard, on_delete=models.CASCADE)
    date = models.DateField()
    probability = models.IntegerField()
    severity = models.IntegerField()
    level = models.IntegerField()
    controls = models.TextField(blank=True)
    evaluated_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='risk_evaluations')
    review_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # Relación a acciones correctivas
    action_item = models.ForeignKey(
        'acciones_correctivas.ActionItem',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Acción correctiva/preventiva asociada (si aplica)"
    )

    def __str__(self):
        return f"{self.hazard} ({self.date})"

    def save(self, *args, **kwargs):
        self.level = self.probability * self.severity
        super().save(*args, **kwargs)

class RiskControl(models.Model):
    risk_assessment = models.ForeignKey('RiskAssessment', on_delete=models.CASCADE, related_name='risk_controls')
    description = models.TextField()
    implemented = models.BooleanField(default=False)
    responsible = models.ForeignKey('empleados.Employee', on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Control for {self.risk_assessment}"

class RiskReview(models.Model):
    risk_assessment = models.ForeignKey('RiskAssessment', on_delete=models.CASCADE, related_name='reviews')
    review_date = models.DateField()
    reviewed_by = models.ForeignKey('empleados.Employee', on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(blank=True)
    risk_level_after_review = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.risk_assessment} on {self.review_date}"