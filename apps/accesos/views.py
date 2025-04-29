from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.utils.auditlogmimix import AuditLogMixin

from .models import AccessLog, RiskAcceptanceForm
from .serializers import AccessLogSerializer, RiskAcceptanceFormSerializer


class AccessLogViewSet(AuditLogMixin, viewsets.ModelViewSet):
    """CRUD + auditoría para registros de ingreso/egreso de empleados."""

    queryset = AccessLog.objects.filter(is_deleted=False)
    serializer_class = AccessLogSerializer
    permission_classes = [AllowAny]

    # --- filtros rápidos opcionales -----------------
    def get_queryset(self):
        qs = super().get_queryset()

        # ?employee=<id>
        if emp_id := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp_id)

        # ?date=YYYY-MM-DD
        if date_str := self.request.query_params.get("date"):
            if dt := parse_date(date_str):
                qs = qs.filter(timestamp__date=dt)

        return qs

    # --- restore lógico -----------------------------
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class RiskAcceptanceFormViewSet(AuditLogMixin, viewsets.ModelViewSet):
    """CRUD + auditoría para formularios de aceptación de riesgo."""

    queryset = RiskAcceptanceForm.objects.filter(is_deleted=False)
    serializer_class = RiskAcceptanceFormSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()

        # ?employee=<id>
        if emp_id := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp_id)

        # ?accepted=true/false
        acc = self.request.query_params.get("accepted")
        if acc is not None:
            qs = qs.filter(accepted=acc.lower() == "true")

        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Formulario restaurado."}, status=status.HTTP_200_OK)
