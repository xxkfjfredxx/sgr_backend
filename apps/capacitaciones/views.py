from rest_framework import viewsets
from .models import TrainingSession, TrainingSessionAttendance
from .serializers import TrainingSessionSerializer, TrainingSessionAttendanceSerializer
from rest_framework.permissions import AllowAny
from apps.auditoria.utils import AuditLogMixin

class TrainingSessionViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer
    permission_classes = [AllowAny]

class TrainingSessionAttendanceViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = TrainingSessionAttendance.objects.all()
    serializer_class = TrainingSessionAttendanceSerializer
    permission_classes = [AllowAny]
