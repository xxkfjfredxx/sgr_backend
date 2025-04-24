from .models import SystemAudit
from django.utils import timezone

class AuditLogMixin:
    """
    Mixin para ViewSets: registra automáticamente create/update/delete.
    Úsalo junto con ModelViewSet.
    """

    def perform_create(self, serializer):
        instance = serializer.save()
        self.log_audit('CREATED', instance, None)
        return instance

    def perform_update(self, serializer):
        old_instance = self.get_object()
        old_data = self.serializer_class(old_instance).data
        instance = serializer.save()
        self.log_audit('UPDATED', instance, old_data)
        return instance

    def perform_destroy(self, instance):
        old_data = self.serializer_class(instance).data
        instance_id = instance.pk
        model_name = instance._meta.db_table
        instance.delete()
        self.log_audit('DELETED', None, old_data, instance_id, model_name)

    def log_audit(self, action, instance, previous_data=None, force_id=None, force_model=None):
        request = self.request
        user = request.user if request.user.is_authenticated else None
        model_name = force_model or instance._meta.db_table if instance else None
        record_id = force_id or (instance.pk if instance else None)
        new_data = self.serializer_class(instance).data if instance else None

        SystemAudit.objects.create(
            user=user,
            action=action,
            affected_table=model_name,
            record_id=record_id,
            previous_data=previous_data,
            new_data=new_data,
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT'),
            created_at=timezone.now()
        )
