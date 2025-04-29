from django.db import models
from django.utils import timezone
from ..auditoria.models import SystemAudit


class AuditLogMixin:
    """
    Mixin para ViewSets: registra automáticamente create/update/delete/restore.
    """

    # ---------- CREATE ----------
    def perform_create(self, serializer):
        extra = {}
        model_cls = getattr(getattr(serializer, "Meta", None), "model", None)
        if model_cls and hasattr(model_cls, "created_by"):
            extra["created_by"] = (
                self.request.user if self.request.user.is_authenticated else None
            )

        instance = serializer.save(**extra)
        self.log_audit("CREATED", instance)
        return instance

    # ---------- UPDATE ----------
    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_data = self.serializer_class(old_instance).data
        instance = serializer.save()
        self.log_audit("UPDATED", instance, old_data)
        return instance

    # ---------- DELETE ----------
    def perform_destroy(self, instance):
        old_data = self.serializer_class(instance).data
        if hasattr(instance, "soft_delete"):
            instance.soft_delete(user=self.request.user)
        else:
            instance.delete()
        self.log_audit("DELETED", None, old_data, instance.pk, instance._meta.db_table)

    # ---------- LOG ----------
    def log_audit(
        self,
        action,
        instance,
        previous_data=None,
        force_id=None,
        force_model=None,
    ):
        req = self.request
        user = req.user if req.user.is_authenticated else None
        model_name = force_model or (instance._meta.db_table if instance else None)
        record_id = force_id or (instance.pk if instance else None)
        new_data = self.serializer_class(instance).data if instance else None

        SystemAudit.objects.create(
            user=user,
            action=action,
            affected_table=model_name,
            record_id=record_id,
            previous_data=previous_data,
            new_data=new_data,
            ip_address=req.META.get("REMOTE_ADDR"),
            user_agent=req.META.get("HTTP_USER_AGENT"),
            created_at=timezone.now(),
        )
