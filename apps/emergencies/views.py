from rest_framework import viewsets
from .models import EmergencyBrigadeMember, EmergencyEquipment, EmergencyDrill
from .serializers import (
    EmergencyBrigadeMemberSerializer, EmergencyEquipmentSerializer, EmergencyDrillSerializer
)

class EmergencyBrigadeMemberViewSet(viewsets.ModelViewSet):
    queryset = EmergencyBrigadeMember.objects.all()
    serializer_class = EmergencyBrigadeMemberSerializer

class EmergencyEquipmentViewSet(viewsets.ModelViewSet):
    queryset = EmergencyEquipment.objects.all()
    serializer_class = EmergencyEquipmentSerializer

class EmergencyDrillViewSet(viewsets.ModelViewSet):
    queryset = EmergencyDrill.objects.all()
    serializer_class = EmergencyDrillSerializer
