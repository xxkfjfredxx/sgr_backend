from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin
from rest_framework.filters import SearchFilter

from .models import Employee, DocumentType, EmployeeDocument
from .serializers import (
    EmployeeSerializer,
    DocumentTypeSerializer,
    EmployeeDocumentSerializer,
)


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class EmployeeViewSet(BaseAuditViewSet):
    queryset = Employee.objects.filter(is_deleted=False)
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        "first_name",
        "last_name",
        "document",
        "user__email",
        "phone_contact",
    ]


class DocumentTypeViewSet(BaseAuditViewSet):
    queryset = DocumentType.objects.filter(is_deleted=False)
    serializer_class = DocumentTypeSerializer


class EmployeeDocumentViewSet(BaseAuditViewSet):
    queryset = EmployeeDocument.objects.filter(is_deleted=False)
    serializer_class = EmployeeDocumentSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        qs = super().get_queryset()
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        if dtype := self.request.query_params.get("document_type"):
            qs = qs.filter(document_type_id=dtype)
        return qs
