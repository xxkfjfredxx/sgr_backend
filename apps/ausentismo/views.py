from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from apps.utils.auditlogmimix import AuditLogMixin
from django.utils.dateparse import parse_date

from .models import Absence
from .serializers import AbsenceSerializer


class AbsenceViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset           = Absence.objects.filter(is_deleted=False)
    serializer_class   = AbsenceSerializer
    permission_classes = [AllowAny]

    # -------- filtros rápidos ----------
    def get_queryset(self):
        qs = super().get_queryset()

        # ?employee=<id>
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)

        # ?type=Licencia
        if typ := self.request.query_params.get("type"):
            qs = qs.filter(absence_type=typ)

        # ?year=2025
        if yr := self.request.query_params.get("year"):
            try:
                qs = qs.filter(start_date__year=int(yr))
            except ValueError:
                pass

        return qs

    # -------- restore lógico -----------
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Ausencia restaurada."}, status=status.HTTP_200_OK)
