from rest_framework import serializers
from .models import AccessLog, RiskAcceptanceForm


class AccessLogSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)

    class Meta:
        model = AccessLog
        fields = [
            "id",
            "employee",
            "employee_name",
            "access_type",
            "timestamp",
            "method",
            "remarks",
            "location",
            "created_at",
            "created_by",
        ]
        read_only_fields = ("created_at", "created_by")


class RiskAcceptanceFormSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)

    class Meta:
        model = RiskAcceptanceForm
        fields = [
            "id",
            "employee",
            "employee_name",
            "task_description",
            "risk_description",
            "date",
            "signature",
            "accepted",
            "ip_address",
            "user_agent",
            "created_at",
            "created_by",
        ]
        read_only_fields = ("created_at", "created_by")
