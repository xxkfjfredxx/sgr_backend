from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import WorkHistory
from .serializers import WorkHistorySerializer

class WorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = WorkHistory.objects.all().order_by('-id')
    serializer_class = WorkHistorySerializer
    permission_classes = [IsAuthenticated]