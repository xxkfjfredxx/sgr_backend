from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.utils.auditlogmimix import AuditLogMixin
from .models import EmploymentLink
from .serializers import EmploymentLinkSerializer


class EmploymentLinkViewSet(AuditLogMixin, viewsets.ModelViewSet):
    """
    CRUD de vínculos laborales con auditoría, soft-delete y filtros.
    """
    queryset           = EmploymentLink.objects.filter(is_deleted=False)
    serializer_class   = EmploymentLinkSerializer
    permission_classes = [AllowAny]           # cámbialo a IsAuthenticated en producción
    filter_backends    = [DjangoFilterBackend, SearchFilter]
    filterset_fields   = ["company", "employee", "status"]
    search_fields      = ["position", "area"]

    # --- filtros extra por fecha -----------------
    def get_queryset(self):
        qs = super().get_queryset()
        if d1 := self.request.query_params.get("from"):
            if (dt := parse_date(d1)):
                qs = qs.filter(start_date__gte=dt)
        if d2 := self.request.query_params.get("to"):
            if (dt := parse_date(d2)):
                qs = qs.filter(start_date__lte=dt)
        return qs

    # --- endpoint para restaurar -----------------
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Vínculo restaurado."}, status=status.HTTP_200_OK)
