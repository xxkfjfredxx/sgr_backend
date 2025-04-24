from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import Company
from .serializers import CompanySerializer
from apps.auditoria.utils import AuditLogMixin

class CompanyViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]
