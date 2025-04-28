from django.db import models
from apps.usuarios.models import User
from apps.empleados.models import Employee

class ChangeRequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pendiente'), ('approved', 'Aprobado'), ('rejected', 'Rechazado')],
        default='pending'
    )

class ChangeEvaluation(models.Model):
    change_request = models.OneToOneField(ChangeRequest, on_delete=models.CASCADE)
    evaluated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    evaluation_comments = models.TextField()
    risk_level = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)
    evaluated_at = models.DateTimeField(auto_now_add=True)

class ChangeImplementation(models.Model):
    change_request = models.OneToOneField(ChangeRequest, on_delete=models.CASCADE)
    implemented_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    implementation_date = models.DateField()
    verification_comments = models.TextField(blank=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='change_verifications')
    verification_date = models.DateField(null=True, blank=True)
