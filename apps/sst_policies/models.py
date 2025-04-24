from django.db import models
from apps.empleados.models import Employee

class SSTPolicy(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(help_text="Descripción corta o alcance de la política")
    document = models.FileField(upload_to='sst_policy/', blank=True, null=True)
    version = models.CharField(max_length=20, default='1.0')
    published_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} v{self.version}"

class PolicyAcceptance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    policy = models.ForeignKey(SSTPolicy, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    acceptance_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('employee', 'policy')
        verbose_name = 'Policy Acceptance'
        verbose_name_plural = 'Policy Acceptances'

    def __str__(self):
        return f"{self.employee} - {self.policy.title} ({'Sí' if self.accepted else 'No'})"
