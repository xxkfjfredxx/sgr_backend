from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import TenantBase          # ⇒ filtra por company_id
from apps.utils.mixins import AuditMixin
from apps.empresa.models import Company
from apps.usuarios.managers import UserManager


class UserRole(TenantBase, AuditMixin, models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT,
                                null=True, blank=True, db_index=True)
    objects = UserManager()
    name         = models.CharField(max_length=50)
    description  = models.TextField(blank=True, null=True)
    permissions  = models.JSONField(blank=True, null=True)
    access_level = models.IntegerField(default=1)
    is_active    = models.BooleanField(default=True, db_index=True)

    class Meta:
        db_table = "user_roles"
        unique_together = (("company", "name"),)   # ← evita duplicados dentro de la empresa
        indexes = [models.Index(fields=["is_deleted"])]

    def __str__(self):
        return f"{self.name} – {self.company.name}"


class User(AuditMixin, AbstractUser):
    role = models.ForeignKey(
        "usuarios.UserRole",
        on_delete=models.RESTRICT,
        null=True, blank=True,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        null=True,          # ← puede ser NULL solo para superuser
        blank=True,
        db_index=True,
    )

    class Meta:
        db_table = "users"
        unique_together = ("username", "company")

    # tenant = company.tenant si existe; None para superuser global
    @property
    def tenant(self):
        return self.company.tenant if self.company else None

    @property
    def active_company(self):
        return getattr(self, "_active_company", None)
