# apps/inspecciones/views.py
from rest_framework import viewsets
from .models import (
    InspectionTemplate, InspectionItem, Inspection,
    InspectionResponse
)
from .serializers import (
    InspectionTemplateSerializer, InspectionItemSerializer,
    InspectionSerializer, InspectionResponseSerializer
)
from rest_framework.permissions import IsAuthenticated

class InspectionTemplateViewSet(viewsets.ModelViewSet):
    queryset = InspectionTemplate.objects.all().order_by('name')
    serializer_class = InspectionTemplateSerializer
    permission_classes = [IsAuthenticated]

class InspectionItemViewSet(viewsets.ModelViewSet):
    queryset = InspectionItem.objects.all()
    serializer_class = InspectionItemSerializer
    permission_classes = [IsAuthenticated]

class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all().order_by('-date')
    serializer_class = InspectionSerializer
    permission_classes = [IsAuthenticated]

class InspectionResponseViewSet(viewsets.ModelViewSet):
    queryset = InspectionResponse.objects.all()
    serializer_class = InspectionResponseSerializer
    permission_classes = [IsAuthenticated]
