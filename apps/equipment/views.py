from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from .models import EquipmentInventory, EquipmentInspection
from .serializers import EquipmentInventorySerializer, EquipmentInspectionSerializer


class EquipmentInventoryViewSet(ModelViewSet):
    queryset = EquipmentInventory.objects.all()
    serializer_class = EquipmentInventorySerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if company_id := self.request.query_params.get("company"):
            qs = qs.filter(company_id=company_id)
        return qs


class EquipmentInspectionViewSet(ModelViewSet):
    queryset = EquipmentInspection.objects.all()
    serializer_class = EquipmentInspectionSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if eq := self.request.query_params.get("equipment"):
            qs = qs.filter(equipment_id=eq)
        return qs
