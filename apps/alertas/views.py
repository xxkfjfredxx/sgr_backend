from rest_framework import viewsets
from .models import DocumentAlert
from .serializers import DocumentAlertSerializer
from rest_framework.permissions import AllowAny

class DocumentAlertViewSet(viewsets.ModelViewSet):
    queryset = DocumentAlert.objects.all()
    serializer_class = DocumentAlertSerializer
    permission_classes = [AllowAny]
