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
from rest_framework.exceptions import NotFound


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


from rest_framework.exceptions import PermissionDenied

class UserViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["role", "is_active"]
    search_fields = ["username", "first_name", "last_name", "email"]
    permission_classes = [EsRolPermitido]
    roles_permitidos = ["Admin", "RRHH"]

    def get_object(self):
        # Para acciones que necesitan acceder incluso si el usuario está eliminado
        if self.action in ["restaurar", "eliminar_definitivamente", "retrieve"]:
            try:
                return User.objects.get(pk=self.kwargs["pk"])
            except User.DoesNotExist:
                raise NotFound("Usuario no encontrado.")
        return super().get_object()

    @action(detail=True, methods=['post'])
    def restaurar(self, request, pk=None):
        user = self.get_object()
        user.is_deleted = False
        user.is_active = True
        user.save()
        return Response({'status': 'usuario restaurado'})
    
    @action(detail=True, methods=['delete'], url_path='eliminar-definitivamente')
    def eliminar_definitivamente(self, request, pk=None):
        user = self.get_object()
        user.delete()
        return Response({'status': 'usuario eliminado de forma permanente'})

    def get_queryset(self):
        user = self.request.user
        empresa_id = self.request.query_params.get("empresa")
        incluir_eliminados = self.request.query_params.get("incluir_eliminados") == "true"
        active_company = getattr(self.request, "active_company", None)

        if not user.is_authenticated:
            raise PermissionDenied("No estás autenticado.")

        if not active_company:
            raise PermissionDenied("No se encontró la empresa activa.")

        if not user.is_superuser and user.company_id != active_company.pk:
            raise PermissionDenied("No tienes permiso para acceder a esta empresa.")

        # 👇 Aquí cambia esto 👇
        qs = User.objects.all() if incluir_eliminados else User.objects.filter(is_deleted=False)

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
