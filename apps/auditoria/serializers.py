from rest_framework import serializers
from .models import SystemAudit
from apps.usuarios.serializers import UserSerializer

class SystemAuditSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)

    class Meta:
        model = SystemAudit
        fields = [
            'id', 'user', 'user_data', 'action', 'affected_table', 'record_id',
            'previous_data', 'new_data', 'ip_address', 'user_agent', 'created_at'
        ]
