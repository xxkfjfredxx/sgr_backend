from rest_framework import serializers
from .models import WorkAccident, WorkAtHeightPermit
from apps.empleados.serializers import EmployeeSerializer


class WorkAccidentSerializer(serializers.ModelSerializer):
    employee_data = EmployeeSerializer(source="employee", read_only=True)

    class Meta:
        model  = WorkAccident
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class WorkAtHeightPermitSerializer(serializers.ModelSerializer):
    employee_data = EmployeeSerializer(source="employee", read_only=True)

    class Meta:
        model  = WorkAtHeightPermit
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
