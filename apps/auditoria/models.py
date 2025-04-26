from django.db import models
from apps.usuarios.models import User
from apps.acciones_correctivas.models import ActionItem 

class SystemAudit(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=100)
    affected_table = models.CharField(max_length=100)
    record_id = models.IntegerField()
    previous_data = models.JSONField(null=True, blank=True)
    new_data = models.JSONField(null=True, blank=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'system_audit'

    def __str__(self):
        return f"{self.action} on {self.affected_table} by {self.user}" if self.user else self.action


class AuditChecklist(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AuditItem(models.Model):
    checklist = models.ForeignKey(AuditChecklist, on_delete=models.CASCADE, related_name='items')
    question = models.CharField(max_length=300)
    expected_result = models.CharField(max_length=300, blank=True)
    evidence_required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.checklist.name} - {self.question[:40]}"

class AuditExecution(models.Model):
    checklist = models.ForeignKey(AuditChecklist, on_delete=models.CASCADE)
    auditor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Abierta")  # Abierta/Cerrada/En seguimiento
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"Auditoría {self.checklist.name} - {self.date}"

class AuditResult(models.Model):
    execution = models.ForeignKey(AuditExecution, on_delete=models.CASCADE, related_name='results')
    item = models.ForeignKey(AuditItem, on_delete=models.CASCADE)
    result = models.CharField(
        max_length=30,
        choices=[
            ("cumple", "Cumple"),
            ("no_cumple", "No cumple"),
            ("parcial", "Cumple parcialmente")
        ]
    )
    evidence_file = models.FileField(upload_to="audit_evidence/", blank=True, null=True)
    observation = models.TextField(blank=True)

    def __str__(self):
        return f"{self.execution} - {self.item.question[:30]}: {self.result}"

class AuditFinding(models.Model):
    execution = models.ForeignKey(AuditExecution, on_delete=models.CASCADE, related_name='findings')
    description = models.TextField()
    severity = models.CharField(
        max_length=20,
        choices=[
            ("Leve", "Leve"),
            ("Moderado", "Moderado"),
            ("Crítico", "Crítico")
        ]
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ("abierto", "Abierto"),
            ("cerrado", "Cerrado"),
            ("seguimiento", "En seguimiento")
        ],
        default="abierto"
    )
    closing_evidence = models.FileField(upload_to="audit_findings_closing/", blank=True, null=True)
    action_item = models.ForeignKey(ActionItem, on_delete=models.SET_NULL, null=True, blank=True, help_text="Acción correctiva asociada (si aplica)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Hallazgo {self.severity} ({self.status})"