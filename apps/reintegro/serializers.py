from rest_framework import serializers
from .models import Reintegro
from apps.empleados.serializers import EmployeeSerializer


class ReintegroSerializer(serializers.ModelSerializer):
    employee_data = EmployeeSerializer(source="employee", read_only=True)

    class Meta:
        model  = Reintegro
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
