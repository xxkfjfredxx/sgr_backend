from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset           = Company.objects.filter(is_deleted=False)
    serializer_class   = CompanySerializer
    permission_classes = [AllowAny]

    # -------- filtros rápidos ----------
    def get_queryset(self):
        qs = super().get_queryset()
        if name := self.request.query_params.get("name"):
            qs = qs.filter(name__icontains=name)
        if sector := self.request.query_params.get("sector"):
            qs = qs.filter(sector__icontains=sector)
        return qs

    # -------- restore lógico -----------
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Empresa restaurada."}, status=status.HTTP_200_OK)
