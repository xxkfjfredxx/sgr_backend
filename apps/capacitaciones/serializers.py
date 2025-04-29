from rest_framework import serializers
from .models import TrainingSession, TrainingSessionAttendance, Certification


class TrainingSessionSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model  = TrainingSession
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class TrainingSessionAttendanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)

    class Meta:
        model  = TrainingSessionAttendance
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class CertificationSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="participant.employee.first_name", read_only=True)
    topic         = serializers.CharField(source="participant.session.topic", read_only=True)

    class Meta:
        model  = Certification
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
