from django.db import models
from apps.empleados.models import Employee
from apps.usuarios.models import User

class ImprovementPlan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('open', 'Abierto'), ('in_progress', 'En Progreso'), ('closed', 'Cerrado')],
        default='open'
    )

    def __str__(self):
        return self.title

class ActionItem(models.Model):
    plan = models.ForeignKey(ImprovementPlan, related_name='actions', on_delete=models.CASCADE)
    description = models.TextField()
    responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    evidence = models.FileField(upload_to='improvement_evidence/', blank=True, null=True)
    comments = models.TextField(blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.plan.title}: {self.description[:50]}"
    
class RiskAction(models.Model):
    risk_assessment = models.ForeignKey(
        'riesgos.RiskAssessment',  # Notación como string 'app.Model'
        on_delete=models.CASCADE,
        related_name='actions'
    )
    description = models.TextField()
    responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    evidence = models.FileField(upload_to='risk_actions_evidence/', blank=True, null=True)
    comments = models.TextField(blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.risk_assessment}: {self.description[:40]}"
