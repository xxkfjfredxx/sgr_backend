from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Reintegro
from .serializers import ReintegroSerializer
from apps.auditoria.utils import AuditLogMixin  # Si quieres auditoría

class ReintegroViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Reintegro.objects.all().order_by('-start_date')
    serializer_class = ReintegroSerializer
    permission_classes = [AllowAny]  # Cambia a IsAuthenticated si lo requieres
