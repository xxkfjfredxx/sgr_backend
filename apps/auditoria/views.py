from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .models import (
    SystemAudit, AuditChecklist, AuditItem, AuditExecution,
    AuditResult, AuditFinding
)
from .serializers import (
    SystemAuditSerializer, AuditChecklistSerializer, AuditItemSerializer,
    AuditExecutionSerializer, AuditResultSerializer, AuditFindingSerializer
)

class SystemAuditViewSet(viewsets.ModelViewSet):
    queryset = SystemAudit.objects.all().order_by('-created_at')
    serializer_class = SystemAuditSerializer
    permission_classes = [AllowAny]  # Solo admin puede ver logs (puedes cambiar)

class AuditChecklistViewSet(viewsets.ModelViewSet):
    queryset = AuditChecklist.objects.all().order_by('-created_at')
    serializer_class = AuditChecklistSerializer
    permission_classes = [AllowAny] 

class AuditItemViewSet(viewsets.ModelViewSet):
    queryset = AuditItem.objects.all()
    serializer_class = AuditItemSerializer
    permission_classes = [AllowAny] 

class AuditExecutionViewSet(viewsets.ModelViewSet):
    queryset = AuditExecution.objects.all().order_by('-date')
    serializer_class = AuditExecutionSerializer
    permission_classes = [AllowAny] 

class AuditResultViewSet(viewsets.ModelViewSet):
    queryset = AuditResult.objects.all()
    serializer_class = AuditResultSerializer
    permission_classes = [AllowAny] 

class AuditFindingViewSet(viewsets.ModelViewSet):
    queryset = AuditFinding.objects.all().order_by('-created_at')
    serializer_class = AuditFindingSerializer
    permission_classes = [AllowAny] 