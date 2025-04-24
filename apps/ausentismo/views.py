from rest_framework import viewsets
from .models import Absence
from .serializers import AbsenceSerializer
from rest_framework.permissions import AllowAny
from apps.auditoria.utils import AuditLogMixin

class AbsenceViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    permission_classes = [AllowAny]
