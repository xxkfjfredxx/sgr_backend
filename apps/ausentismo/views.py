from rest_framework import viewsets
from .models import Absence
from .serializers import AbsenceSerializer
from rest_framework.permissions import AllowAny

class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    permission_classes = [AllowAny]
