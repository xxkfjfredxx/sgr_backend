from rest_framework import serializers
from .models import EmergencyBrigadeMember, EmergencyEquipment, EmergencyDrill

class EmergencyBrigadeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyBrigadeMember
        fields = '__all__'

class EmergencyEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyEquipment
        fields = '__all__'

class EmergencyDrillSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyDrill
        fields = '__all__'
