from rest_framework import serializers
from .models import (
    SystemAudit, AuditChecklist, AuditItem, AuditExecution,
    AuditResult, AuditFinding
)
from apps.acciones_correctivas.serializers import ActionItemSerializer

class SystemAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAudit
        fields = '__all__'

class AuditChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditChecklist
        fields = '__all__'

class AuditItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditItem
        fields = '__all__'

class AuditExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditExecution
        fields = '__all__'

class AuditResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditResult
        fields = '__all__'

class AuditFindingSerializer(serializers.ModelSerializer):
    action_item = ActionItemSerializer(read_only=True)
    class Meta:
        model = AuditFinding
        fields = '__all__'