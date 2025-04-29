from rest_framework import serializers
from .models import SupportTicket, MaintenanceSchedule, MaintenanceRecord


class SupportTicketSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(
        source="created_by.username", read_only=True
    )
    assigned_to_username = serializers.CharField(
        source="assigned_to.username", read_only=True
    )

    class Meta:
        model = SupportTicket
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class MaintenanceScheduleSerializer(serializers.ModelSerializer):
    responsible_username = serializers.CharField(
        source="responsible.username", read_only=True
    )

    class Meta:
        model = MaintenanceSchedule
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class MaintenanceRecordSerializer(serializers.ModelSerializer):
    schedule_title = serializers.CharField(source="schedule.title", read_only=True)

    class Meta:
        model = MaintenanceRecord
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
