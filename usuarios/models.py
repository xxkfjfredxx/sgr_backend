from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRole(models.Model):  # "Tabla de Roles de Usuario"
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    permissions = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_roles'  # "Tabla en base de datos: Roles de Usuario"

    def __str__(self):
        return self.name


class User(AbstractUser):  # "Tabla de Usuarios"
    role = models.ForeignKey(UserRole, on_delete=models.RESTRICT)  # "Rol del usuario"

    class Meta:
        db_table = 'users'  # "Tabla en base de datos: Usuarios"