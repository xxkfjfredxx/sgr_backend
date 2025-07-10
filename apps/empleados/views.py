from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django.db import models
from django.db.models import Subquery
from django.core.exceptions import PermissionDenied
from apps.utils.auditlogmimix import AuditLogMixin
from apps.vinculaciones.models import EmploymentLink

from .models import Employee, DocumentType, EmployeeDocument, DocumentCategory
from .serializers import (
    EmployeeSerializer,
    DocumentTypeSerializer,
    EmployeeDocumentSerializer,
    DocumentCategorySerializer,
)


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


# ─── EmployeeViewSet ───────────────────────────────────────────────
class EmployeeViewSet(BaseAuditViewSet):
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        "first_name",
        "last_name",
        "document",
        "user__email",
        "phone_contact",
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if not hasattr(self.request, 'active_company'):
            raise PermissionDenied("No se encontró la compañía activa en la solicitud")
        context['request'] = self.request
        print(f"ACTIVE COMPANY in context: {self.request.active_company}")  # Verifica que esté presente
        return context

    def get_queryset(self):
        print("🔥 GET_QUERYSET EJECUTADO")

        user = self.request.user
        if hasattr(self.request, 'active_company'):
            qs = Employee.objects.filter(company=self.request.active_company)
        else:
            raise PermissionDenied("No se encontró la compañía activa en la solicitud")

        if hasattr(user, "active_company") and user.active_company:
            qs = qs.filter(company=user.active_company)

        if name := self.request.query_params.get("name"):
            qs = qs.filter(
                models.Q(first_name__icontains=name)
                | models.Q(last_name__icontains=name)
            )

        if doc := self.request.query_params.get("document"):
            qs = qs.filter(document__icontains=doc)

        return qs.distinct()


class EmployeeDocumentViewSet(BaseAuditViewSet):
    queryset = EmployeeDocument.objects.filter(is_deleted=False)
    serializer_class = EmployeeDocumentSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(employee__company=self.request.user.active_company)
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        if dtype := self.request.query_params.get("document_type"):
            qs = qs.filter(document_type_id=dtype)
        return qs


# ─── Categorías (solo lectura) ───────────────────────────────
class DocumentCategoryViewSet(BaseAuditViewSet):
    queryset = DocumentCategory.objects.filter(is_deleted=False)
    serializer_class = DocumentCategorySerializer
    http_method_names = ["get", "head", "options"]


# ─── Tipos de documento (solo lectura) ───────────────────────
class DocumentTypeViewSet(BaseAuditViewSet):
    queryset = DocumentType.objects.filter(is_deleted=False)
    serializer_class = DocumentTypeSerializer
    http_method_names = ["get", "head", "options"]

    def get_queryset(self):
        qs = super().get_queryset()
        if cat := self.request.query_params.get("category"):
            qs = qs.filter(category_id=cat)
        return qs
