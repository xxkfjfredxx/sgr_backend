from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import Reintegro
from .serializers import ReintegroSerializer


class ReintegroViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Reintegro.objects.filter(is_deleted=False)
    serializer_class = ReintegroSerializer
    permission_classes = [AllowAny]

    # ---------- filtros rápidos ----------
    def get_queryset(self):
        qs = super().get_queryset()

        # ?employee=<id>
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)

        # ?successful=true/false
        if suc := self.request.query_params.get("successful"):
            qs = qs.filter(successful=suc.lower() == "true")

        # ?date_from=YYYY-MM-DD   &   ?date_to=YYYY-MM-DD
        if df := self.request.query_params.get("date_from"):
            if d1 := parse_date(df):
                qs = qs.filter(start_date__gte=d1)
        if dt := self.request.query_params.get("date_to"):
            if d2 := parse_date(dt):
                qs = qs.filter(start_date__lte=d2)

        return qs

    # ---------- restaurar lógico ----------
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Reintegro restaurado."}, status=status.HTTP_200_OK)
