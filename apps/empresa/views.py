from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q  # ✅ Asegúrate de importar esto

from apps.utils.auditlogmimix import AuditLogMixin
from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(AuditLogMixin, viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]  # ← solo usuarios autenticados

    def get_queryset(self):
        user = self.request.user

        # ✅ SUPERADMIN: acceso total
        if user.is_superuser:
            qs = Company.objects.filter(is_deleted=False)

        # ✅ ADMIN GLOBAL: sin empresa asociada ni relación employee
        elif (
            user.role
            and user.role.name.lower() == "admin"
            and not hasattr(user, "employee")
            and not user.role.company  # 👈 Verifica que el rol no esté ligado a una empresa
        ):
            qs = Company.objects.filter(is_deleted=False)

        # 🚫 DEMÁS USUARIOS: sin acceso
        else:
            qs = Company.objects.none()

        # 🔍 Filtros de búsqueda
        if search := self.request.query_params.get("search"):
            qs = qs.filter(Q(name__icontains=search) | Q(nit__icontains=search))
        if name := self.request.query_params.get("name"):
            qs = qs.filter(name__icontains=name)
        if sector := self.request.query_params.get("sector"):
            qs = qs.filter(sector__icontains=sector)

        return qs

    # -------- restore lógico -----------
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
