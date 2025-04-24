from rest_framework import viewsets
from .models import MedicalExam
from .serializers import MedicalExamSerializer
from rest_framework.permissions import AllowAny
from apps.auditoria.utils import AuditLogMixin

class MedicalExamViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = MedicalExam.objects.all()
    serializer_class = MedicalExamSerializer
    permission_classes = [AllowAny]
