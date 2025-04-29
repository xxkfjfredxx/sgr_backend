from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import WorkAccident, WorkAtHeightPermit
from .serializers import WorkAccidentSerializer, WorkAtHeightPermitSerializer


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


# ---------------- Accidentes / Incidentes -----------------
class WorkAccidentViewSet(BaseAuditViewSet):
    queryset = WorkAccident.objects.filter(is_deleted=False)
    serializer_class = WorkAccidentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        if typ := self.request.query_params.get("type"):
            qs = qs.filter(incident_type=typ)
        if sev := self.request.query_params.get("severity"):
            qs = qs.filter(severity=sev)
        if d1 := self.request.query_params.get("from"):
            if dt := parse_date(d1):
                qs = qs.filter(date__gte=dt)
        return qs


# ---------------- Permisos de Trabajo en Alturas -----------
class WorkAtHeightPermitViewSet(BaseAuditViewSet):
    queryset = WorkAtHeightPermit.objects.filter(is_deleted=False)
    serializer_class = WorkAtHeightPermitSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        if app := self.request.query_params.get("approved"):
            qs = qs.filter(approved=app.lower() == "true")
        return qs
