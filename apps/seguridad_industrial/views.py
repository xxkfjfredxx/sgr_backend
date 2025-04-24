from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import WorkAccident, WorkAtHeightPermit
from .serializers import WorkAccidentSerializer, WorkAtHeightPermitSerializer
from apps.auditoria.utils import AuditLogMixin

class WorkAccidentViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = WorkAccident.objects.all().order_by('-date')
    serializer_class = WorkAccidentSerializer
    permission_classes = [AllowAny]

class WorkAtHeightPermitViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = WorkAtHeightPermit.objects.all().order_by('-date')
    serializer_class = WorkAtHeightPermitSerializer
    permission_classes = [AllowAny]
