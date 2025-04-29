from rest_framework import serializers
from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)
    contractor_name = serializers.CharField(source="contractor.name", read_only=True)

    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
