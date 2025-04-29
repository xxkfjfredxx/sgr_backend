from rest_framework import serializers
from .models import SSTPolicy, PolicyAcceptance


class SSTPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = SSTPolicy
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class PolicyAcceptanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)
    policy_title = serializers.CharField(source="policy.title", read_only=True)

    class Meta:
        model = PolicyAcceptance
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
