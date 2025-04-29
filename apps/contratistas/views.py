from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.utils.auditlogmimix import AuditLogMixin

from .models import ContractorCompany, ContractorContact
from .serializers import ContractorCompanySerializer, ContractorContactSerializer


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    # filtro común por nombre ?name=
    def get_queryset(self):
        qs = super().get_queryset()
        if nm := self.request.query_params.get("name"):
            qs = qs.filter(name__icontains=nm)
        return qs

    # restaurar borrado lógico
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class ContractorCompanyViewSet(BaseAuditViewSet):
    """CRUD de Empresas Contratistas"""

    queryset = ContractorCompany.objects.filter(is_deleted=False)
    serializer_class = ContractorCompanySerializer

    # filtro extra: ?active=true/false
    def get_queryset(self):
        qs = super().get_queryset()
        if act := self.request.query_params.get("active"):
            qs = qs.filter(active=act.lower() == "true")
        return qs


class ContractorContactViewSet(BaseAuditViewSet):
    """CRUD de Contactos de Contratistas"""

    queryset = ContractorContact.objects.filter(is_deleted=False)
    serializer_class = ContractorContactSerializer

    # filtro extra: ?contractor=<id>
    def get_queryset(self):
        qs = super().get_queryset()
        if cid := self.request.query_params.get("contractor"):
            qs = qs.filter(contractor_id=cid)
        return qs
