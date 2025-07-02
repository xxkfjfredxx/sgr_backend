from rest_framework import viewsets, filters, status
from .models import User, UserRole
from .serializers import UserSerializer, UserRoleSerializer
from .permissions import EsRolPermitido
from apps.utils.auditlogmimix import AuditLogMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied, ValidationError


class UserRoleViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = UserRole.objects.filter(is_deleted=False)
    serializer_class = UserRoleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    roles_permitidos = ["Admin"]
    permission_classes = [EsRolPermitido]

    def perform_create(self, serializer):
        company_id = self.request.data.get("company")
        if not company_id:
            raise ValidationError({"company": "Este campo es obligatorio."})

        user = self.request.user
        if not user.is_superuser:
            # El usuario sólo puede usar su propia empresa
            if not user.role or user.role.company_id != int(company_id):
                raise PermissionDenied("No puedes crear roles en otra empresa.")

        serializer.save(company_id=company_id)

    # ✅ Filtro por empresa
    def get_queryset(self):
        qs = super().get_queryset()
        empresa_id = self.request.query_params.get("empresa")
        if empresa_id:
            qs = qs.filter(company_id=empresa_id)
        return qs


class UserViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["role", "is_active"]
    search_fields = ["username", "first_name", "last_name", "email"]
    permission_classes = [EsRolPermitido]
    roles_permitidos = ["Admin", "RRHH"]

    # ✅ Filtro robusto por empresa: por employee o por rol
    def get_queryset(self):
        qs = super().get_queryset()
        empresa_id = self.request.query_params.get("empresa")
        if empresa_id:
            qs = qs.filter(
                Q(employee__company_id=empresa_id) | Q(role__company_id=empresa_id)
            ).distinct()
        return qs


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)
