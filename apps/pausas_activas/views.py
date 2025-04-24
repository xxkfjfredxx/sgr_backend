from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ActivePauseSession, ActivePauseAttendance
from .serializers import ActivePauseSessionSerializer, ActivePauseAttendanceSerializer

class ActivePauseSessionViewSet(viewsets.ModelViewSet):
    queryset = ActivePauseSession.objects.all().order_by('-date')
    serializer_class = ActivePauseSessionSerializer
    permission_classes = [AllowAny]

class ActivePauseAttendanceViewSet(viewsets.ModelViewSet):
    queryset = ActivePauseAttendance.objects.all()
    serializer_class = ActivePauseAttendanceSerializer
    permission_classes = [AllowAny]
