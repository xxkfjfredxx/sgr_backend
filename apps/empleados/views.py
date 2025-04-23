from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from apps.empleados.models import Employee, DocumentType, EmployeeDocument
from .serializers import EmployeeSerializer, DocumentTypeSerializer, EmployeeDocumentSerializer

# 👇 AGREGADO: ViewSet para Employee
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]

class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all().order_by('name')
    serializer_class = DocumentTypeSerializer
    permission_classes = [AllowAny]

class EmployeeDocumentViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDocument.objects.all().order_by('-uploaded_at')
    serializer_class = EmployeeDocumentSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        employee_id = self.request.query_params.get('employee')
        if employee_id:
            queryset = queryset.filter(employee_id=employee_id)
        return queryset
