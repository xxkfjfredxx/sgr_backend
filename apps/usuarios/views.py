from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import EsRolPermitido
from apps.utils.auditlogmimix import AuditLogMixin
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class UserRoleViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset         = UserRole.objects.filter(is_deleted=False)
    serializer_class = UserRoleSerializer
    filter_backends  = [filters.SearchFilter]
    search_fields    = ["name"]
    roles_permitidos = ["Admin"]         # ejemplo de uso de tu permiso
    permission_classes = [EsRolPermitido]


class UserViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset         = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer
    filter_backends  = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["role", "is_active"]
    search_fields    = ["username", "first_name", "last_name", "email"]
    permission_classes = [EsRolPermitido]
    roles_permitidos = ["Admin", "RRHH"]

class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)