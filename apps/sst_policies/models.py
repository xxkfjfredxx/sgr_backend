from django.db import models
from apps.empresa.models import Company
from apps.utils.mixins import AuditMixin
from apps.empleados.models import Employee


class SSTPolicy(AuditMixin, models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    document = models.FileField(upload_to="sst_policy/", blank=True, null=True)
    version = models.CharField(max_length=20, default="1.0")
    published_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return f"{self.title} v{self.version}"


class PolicyAcceptance(AuditMixin, models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    policy = models.ForeignKey(SSTPolicy, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("employee", "policy")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.employee} – {self.policy}"
