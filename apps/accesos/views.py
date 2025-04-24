from rest_framework import viewsets
from .models import AccessLog, RiskAcceptanceForm
from .serializers import AccessLogSerializer, RiskAcceptanceFormSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny

class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = AccessLog.objects.all().order_by('-timestamp')
    serializer_class = AccessLogSerializer
    permission_classes = [AllowAny]

class RiskAcceptanceFormViewSet(viewsets.ModelViewSet):
    queryset = RiskAcceptanceForm.objects.all().order_by('-date')
    serializer_class = RiskAcceptanceFormSerializer
    permission_classes = [AllowAny]