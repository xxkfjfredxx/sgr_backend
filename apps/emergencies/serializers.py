from rest_framework import serializers
from .models import EmergencyBrigadeMember, EmergencyEquipment, EmergencyDrill


class EmergencyBrigadeMemberSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)

    class Meta:
        model = EmergencyBrigadeMember
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class EmergencyEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyEquipment
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class EmergencyDrillSerializer(serializers.ModelSerializer):
    participant_ids = serializers.PrimaryKeyRelatedField(
        source="participants", many=True, read_only=True
    )

    class Meta:
        model = EmergencyDrill
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
