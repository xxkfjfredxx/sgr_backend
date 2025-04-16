from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SystemAudit
from .serializers import SystemAuditSerializer

class SystemAuditViewSet(viewsets.ModelViewSet):
    queryset = SystemAudit.objects.all().order_by('-id')
    serializer_class = SystemAuditSerializer
    permission_classes = [IsAuthenticated]

