from rest_framework import viewsets
from .models import WorkAccident
from .serializers import WorkAccidentSerializer
from rest_framework.permissions import AllowAny

class WorkAccidentViewSet(viewsets.ModelViewSet):
    queryset = WorkAccident.objects.all()
    serializer_class = WorkAccidentSerializer
    permission_classes = [AllowAny]
