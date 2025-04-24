from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ErgonomicAssessment, ARO, ATS
from .serializers import ErgonomicAssessmentSerializer, AROSerializer, ATSSerializer

class ErgonomicAssessmentViewSet(viewsets.ModelViewSet):
    queryset = ErgonomicAssessment.objects.all().order_by('-date')
    serializer_class = ErgonomicAssessmentSerializer
    permission_classes = [AllowAny]

class AROViewSet(viewsets.ModelViewSet):
    queryset = ARO.objects.all().order_by('-date')
    serializer_class = AROSerializer
    permission_classes = [AllowAny]

class ATSViewSet(viewsets.ModelViewSet):
    queryset = ATS.objects.all().order_by('-date')
    serializer_class = ATSSerializer
    permission_classes = [AllowAny]
