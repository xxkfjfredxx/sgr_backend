from rest_framework import viewsets
from .models import Area, Hazard, RiskAssessment,RiskControl, RiskReview
from .serializers import AreaSerializer, HazardSerializer, RiskAssessmentSerializer, RiskControlSerializer, RiskReviewSerializer

from rest_framework.permissions import IsAuthenticated,AllowAny

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all().order_by('name')
    serializer_class = AreaSerializer
    permission_classes = [AllowAny]

class HazardViewSet(viewsets.ModelViewSet):
    queryset = Hazard.objects.all()
    serializer_class = HazardSerializer
    permission_classes = [AllowAny]

class RiskAssessmentViewSet(viewsets.ModelViewSet):
    queryset = RiskAssessment.objects.all().order_by('-date')
    serializer_class = RiskAssessmentSerializer
    permission_classes = [AllowAny]

class RiskControlViewSet(viewsets.ModelViewSet):
    queryset = RiskControl.objects.all().order_by('-created_at')
    serializer_class = RiskControlSerializer
    permission_classes = [AllowAny]

class RiskReviewViewSet(viewsets.ModelViewSet):
    queryset = RiskReview.objects.all().order_by('-created_at')
    serializer_class = RiskReviewSerializer
    permission_classes = [AllowAny]