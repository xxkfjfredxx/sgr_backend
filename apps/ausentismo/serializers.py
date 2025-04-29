from rest_framework import serializers
from .models import Absence


class AbsenceSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)

    class Meta:
        model = Absence
        fields = "__all__"
        read_only_fields = ("created_at", "created_by", "updated_at")
