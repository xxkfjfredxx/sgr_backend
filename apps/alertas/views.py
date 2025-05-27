from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.utils.auditlogmimix import AuditLogMixin

from .models import DocumentAlert
from .serializers import DocumentAlertSerializer


class DocumentAlertViewSet(AuditLogMixin, viewsets.ModelViewSet):
    """Alertas de vencimiento de documentos (con auditoría)."""

    queryset = DocumentAlert.objects.filter(is_deleted=False)
    serializer_class = DocumentAlertSerializer
    permission_classes = [AllowAny]

    # ------------- filtros rápidos -----------------
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(employee__company=self.request.user.active_company)
        # ?employee=<id>
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)

        # ?active=true/false
        if act := self.request.query_params.get("active"):
            qs = qs.filter(active=act.lower() == "true")

        # ?expired=true  (filtra vencidas a la fecha de hoy)
        if self.request.query_params.get("expired") == "true":
            qs = qs.filter(expiration_date__lt=timezone.localdate())

        return qs

    # --------- restore lógico ----------
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Alerta restaurada."}, status=status.HTTP_200_OK)
