from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import EmergencyBrigadeMember, EmergencyEquipment, EmergencyDrill
from .serializers import (
    EmergencyBrigadeMemberSerializer,
    EmergencyEquipmentSerializer,
    EmergencyDrillSerializer,
)


# --------- ViewSet base con funciones comunes -------------
class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if name := self.request.query_params.get("name"):
            qs = qs.filter(employee__first_name__icontains=name)  # para BrigadeMember
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class EmergencyBrigadeMemberViewSet(BaseAuditViewSet):
    queryset = EmergencyBrigadeMember.objects.filter(is_deleted=False)
    serializer_class = EmergencyBrigadeMemberSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if role := self.request.query_params.get("role"):
            qs = qs.filter(role=role)
        if act := self.request.query_params.get("active"):
            qs = qs.filter(active=act.lower() == "true")
        return qs


class EmergencyEquipmentViewSet(BaseAuditViewSet):
    queryset = EmergencyEquipment.objects.filter(is_deleted=False)
    serializer_class = EmergencyEquipmentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if typ := self.request.query_params.get("type"):
            qs = qs.filter(type=typ)
        if loc := self.request.query_params.get("location"):
            qs = qs.filter(location__icontains=loc)
        return qs


class EmergencyDrillViewSet(BaseAuditViewSet):
    queryset = EmergencyDrill.objects.filter(is_deleted=False)
    serializer_class = EmergencyDrillSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if dtype := self.request.query_params.get("drill_type"):
            qs = qs.filter(drill_type=dtype)
        if date_str := self.request.query_params.get("date"):
            if d := parse_date(date_str):
                qs = qs.filter(date=d)
        return qs
