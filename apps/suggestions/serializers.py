from rest_framework import serializers
from .models import SuggestionBox
from apps.empleados.serializers import EmployeeSerializer


class SuggestionBoxSerializer(serializers.ModelSerializer):
    employee_data = EmployeeSerializer(source="employee", read_only=True)

    class Meta:
        model  = SuggestionBox
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
