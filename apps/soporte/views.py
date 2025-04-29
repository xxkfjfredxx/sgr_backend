from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import SupportTicket, MaintenanceSchedule, MaintenanceRecord
from .serializers import (
    SupportTicketSerializer,
    MaintenanceScheduleSerializer,
    MaintenanceRecordSerializer,
)


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class SupportTicketViewSet(BaseAuditViewSet):
    queryset = SupportTicket.objects.filter(is_deleted=False)
    serializer_class = SupportTicketSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if st := self.request.query_params.get("status"):
            qs = qs.filter(status=st)
        if usr := self.request.query_params.get("assigned_to"):
            qs = qs.filter(assigned_to_id=usr)
        return qs


class MaintenanceScheduleViewSet(BaseAuditViewSet):
    queryset = MaintenanceSchedule.objects.filter(is_deleted=False)
    serializer_class = MaintenanceScheduleSerializer


class MaintenanceRecordViewSet(BaseAuditViewSet):
    queryset = MaintenanceRecord.objects.filter(is_deleted=False)
    serializer_class = MaintenanceRecordSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if sch := self.request.query_params.get("schedule"):
            qs = qs.filter(schedule_id=sch)
        return qs
