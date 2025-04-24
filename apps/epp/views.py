from rest_framework import viewsets
from .models import EPPItem, EPPAssignment
from .serializers import EPPItemSerializer, EPPAssignmentSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny

class EPPItemViewSet(viewsets.ModelViewSet):
    queryset = EPPItem.objects.all().order_by('name')
    serializer_class = EPPItemSerializer
    permission_classes = [AllowAny]

class EPPAssignmentViewSet(viewsets.ModelViewSet):
    queryset = EPPAssignment.objects.all().order_by('-assigned_at')
    serializer_class = EPPAssignmentSerializer
    permission_classes = [AllowAny]