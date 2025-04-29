from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import SSTPolicy, PolicyAcceptance
from .serializers import SSTPolicySerializer, PolicyAcceptanceSerializer


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class SSTPolicyViewSet(BaseAuditViewSet):
    queryset = SSTPolicy.objects.filter(is_deleted=False)
    serializer_class = SSTPolicySerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if active := self.request.query_params.get("active"):
            qs = qs.filter(active=active.lower() == "true")
        return qs


class PolicyAcceptanceViewSet(BaseAuditViewSet):
    queryset = PolicyAcceptance.objects.filter(is_deleted=False)
    serializer_class = PolicyAcceptanceSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if pol := self.request.query_params.get("policy"):
            qs = qs.filter(policy_id=pol)
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        return qs
