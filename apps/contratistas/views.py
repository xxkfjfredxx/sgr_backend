from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ContractorCompany, ContractorContact
from .serializers import ContractorCompanySerializer, ContractorContactSerializer
from apps.auditoria.utils import AuditLogMixin

class ContractorCompanyViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = ContractorCompany.objects.all().order_by('name')
    serializer_class = ContractorCompanySerializer
    permission_classes = [AllowAny]

class ContractorContactViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = ContractorContact.objects.all()
    serializer_class = ContractorContactSerializer
    permission_classes = [AllowAny]
