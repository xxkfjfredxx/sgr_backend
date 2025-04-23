from rest_framework import viewsets
from .models import TrainingSession, TrainingSessionAttendance
from .serializers import TrainingSessionSerializer, TrainingSessionAttendanceSerializer
from rest_framework.permissions import AllowAny

class TrainingSessionViewSet(viewsets.ModelViewSet):
    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer
    permission_classes = [AllowAny]

class TrainingSessionAttendanceViewSet(viewsets.ModelViewSet):
    queryset = TrainingSessionAttendance.objects.all()
    serializer_class = TrainingSessionAttendanceSerializer
    permission_classes = [AllowAny]
