from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import WorkHistory
from .serializers import WorkHistorySerializer
from apps.auditoria.utils import AuditLogMixin

class WorkHistoryViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = WorkHistory.objects.all().order_by('-id')
    serializer_class = WorkHistorySerializer
    permission_classes = [AllowAny]