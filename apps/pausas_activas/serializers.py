from rest_framework import serializers
from .models import ActivePauseSession, ActivePauseAttendance
from apps.empleados.serializers import EmployeeSerializer


class ActivePauseAttendanceSerializer(serializers.ModelSerializer):
    employee_data = EmployeeSerializer(source="employee", read_only=True)

    class Meta:
        model = ActivePauseAttendance
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class ActivePauseSessionSerializer(serializers.ModelSerializer):
    attendances = ActivePauseAttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = ActivePauseSession
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
