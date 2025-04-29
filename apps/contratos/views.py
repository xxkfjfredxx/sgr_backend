from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny            # cámbialo luego
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from apps.utils.auditlogmimix import AuditLogMixin
from .models      import Contract
from .serializers import ContractSerializer


class ContractViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset           = Contract.objects.filter(is_deleted=False)
    serializer_class   = ContractSerializer
    permission_classes = [AllowAny]

    filter_backends  = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["company", "employee", "status", "contract_type"]
    search_fields    = ["employee__first_name", "employee__last_name"]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Contrato restaurado."}, status=status.HTTP_200_OK)
