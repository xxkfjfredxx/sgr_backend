from rest_framework import viewsets
from .models import SSTPolicy, PolicyAcceptance
from .serializers import SSTPolicySerializer, PolicyAcceptanceSerializer

class SSTPolicyViewSet(viewsets.ModelViewSet):
    queryset = SSTPolicy.objects.all().order_by('-published_date')
    serializer_class = SSTPolicySerializer

class PolicyAcceptanceViewSet(viewsets.ModelViewSet):
    queryset = PolicyAcceptance.objects.all().order_by('-acceptance_date')
    serializer_class = PolicyAcceptanceSerializer
