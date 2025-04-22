from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.empleados.models import Employee,DocumentType, EmployeeDocument
from rest_framework.permissions import AllowAny
from .serializers import EmployeeSerializer,DocumentTypeSerializer, EmployeeDocumentSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]


class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all().order_by('name')
    serializer_class = DocumentTypeSerializer


class EmployeeDocumentViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDocument.objects.all().order_by('-uploaded_at')
    serializer_class = EmployeeDocumentSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]  # 👈 esto
    