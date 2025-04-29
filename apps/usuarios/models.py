from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.utils.mixins import AuditMixin

class UserRole(AuditMixin, models.Model):      # ← cambia la herencia
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    permissions = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # created_at y updated_at ya los da AuditMixin

    class Meta:
        db_table = "user_roles"

class User(AuditMixin, AbstractUser):
    role = models.ForeignKey(UserRole, on_delete=models.RESTRICT, null=True, blank=True)
    class Meta:
        db_table = "users"