from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.utils.mixins import AuditMixin


class UserRole(AuditMixin, models.Model):
    name = models.CharField(max_length=50, unique=True)  # índice implícito por UNIQUE
    description = models.TextField(blank=True, null=True)
    permissions = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        db_table = "user_roles"
        indexes = [
            models.Index(fields=["is_deleted"]),
        ]


class User(AuditMixin, AbstractUser):
    role = models.ForeignKey(UserRole, on_delete=models.RESTRICT, null=True, blank=True)

    class Meta:
        db_table = "users"

    @property
    def active_company(self):
        return getattr(self, "_active_company", None)
