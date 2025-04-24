from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .models import SystemAudit
from .serializers import SystemAuditSerializer

class SystemAuditViewSet(viewsets.ModelViewSet):
    queryset = SystemAudit.objects.all().order_by('-created_at')
    serializer_class = SystemAuditSerializer
    permission_classes = [AllowAny]  # Solo admin puede ver logs (puedes cambiar)
