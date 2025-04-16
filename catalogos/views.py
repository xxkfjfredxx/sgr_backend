from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Branch, Position, WorkArea, DocumentType
from .serializers import BranchSerializer, PositionSerializer, WorkAreaSerializer, DocumentTypeSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('name')
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated]

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all().order_by('name')
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticated]

class WorkAreaViewSet(viewsets.ModelViewSet):
    queryset = WorkArea.objects.all().order_by('name')
    serializer_class = WorkAreaSerializer
    permission_classes = [IsAuthenticated]

class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all().order_by('name')
    serializer_class = DocumentTypeSerializer
    permission_classes = [IsAuthenticated]
