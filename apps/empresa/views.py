from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
import uuid
from rest_framework import serializers

from apps.utils.auditlogmimix import AuditLogMixin
from .models import Company
from apps.tenants.models import Tenant
from .serializers import CompanySerializer


class CompanyViewSet(AuditLogMixin, viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            qs = Company.objects.filter(is_deleted=False)

        elif (
            user.role
            and user.role.name.lower() == "admin"
            and not hasattr(user, "employee")
            and not user.role.company
        ):
            qs = Company.objects.filter(is_deleted=False)

        else:
            qs = Company.objects.none()

        if search := self.request.query_params.get("search"):
            qs = qs.filter(Q(name__icontains=search) | Q(nit__icontains=search))
        if name := self.request.query_params.get("name"):
            qs = qs.filter(name__icontains=name)
        if sector := self.request.query_params.get("sector"):
            qs = qs.filter(sector__icontains=sector)

        return qs

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_superuser:
            # ⚡️ El superusuario crea automáticamente el Tenant al crear la Empresa
            empresa_nombre = self.request.data.get('name')
            if not empresa_nombre:
                raise serializers.ValidationError(
                    {"name": "Este campo es obligatorio para crear la empresa."}
                )

            # Crear Tenant automáticamente
            tenant = Tenant.objects.create(
                name=empresa_nombre,
                db_label=f"tenant_{uuid.uuid4().hex[:8]}"
            )

            # Generar db_label único para la Company
            db_label = f"company_{uuid.uuid4().hex[:8]}"

            # Guardar la nueva Company vinculada al Tenant creado
            serializer.save(tenant=tenant, db_label=db_label)
            return

        # ⚡️ Usuarios normales → usan su propio Tenant
        tenant = None

        if hasattr(user, 'employee') and user.employee and user.employee.company:
            tenant = user.employee.company.tenant
        elif user.role and user.role.company and user.role.company.tenant:
            tenant = user.role.company.tenant

        if not tenant:
            raise serializers.ValidationError("No se pudo determinar el tenant para este usuario.")

        db_label = f"company_{uuid.uuid4().hex[:8]}"
        serializer.save(tenant=tenant, db_label=db_label)

    @action(
        detail=False,
        methods=["get"],
        url_path="my-companies",
        permission_classes=[IsAuthenticated],
    )
    def my_companies(self, request):
        user = request.user

        if user.is_superuser or (
            user.role
            and user.role.name.lower() == "admin"
            and not hasattr(user, "employee")
            and not user.role.company
        ):
            qs = self.get_queryset()

        elif hasattr(user, "employee"):
            empresa = user.employee.empresa
            qs = (
                Company.objects.filter(id=empresa.id)
                if empresa
                else Company.objects.none()
            )

        elif user.role and user.role.company:
            qs = Company.objects.filter(id=user.role.company.id)

        else:
            qs = Company.objects.none()

        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
