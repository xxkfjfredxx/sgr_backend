from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import Branch, Position, WorkArea
from .serializers import BranchSerializer, PositionSerializer, WorkAreaSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('name')
    serializer_class = BranchSerializer
    permission_classes = [AllowAny]

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all().order_by('name')
    serializer_class = PositionSerializer
    permission_classes = [AllowAny]

class WorkAreaViewSet(viewsets.ModelViewSet):
    queryset = WorkArea.objects.all().order_by('name')
    serializer_class = WorkAreaSerializer
    permission_classes = [AllowAny]
