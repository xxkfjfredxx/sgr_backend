from django.db import models
from apps.usuarios.models import User

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
