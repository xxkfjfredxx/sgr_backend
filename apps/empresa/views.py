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


# apps/empresa/views.py
import logging

# Configura el logger
logger = logging.getLogger(__name__)

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            qs = Company.objects.all()
        else:
            qs = Company.objects.none()
        return qs

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_superuser:
            raise serializers.ValidationError({"detail": "Solo el superusuario puede crear empresas."})
        serializer.save()

    @action(detail=False, methods=["get"], url_path="my-companies")
    def my_companies(self, request):
        user = request.user

        if user.is_superuser:
            qs = self.get_queryset()
        else:
            qs = Company.objects.none()

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="me")
    def me(self, request):
        company = getattr(request, "active_company", None)

        if not company:
            # Si no existe 'active_company', intenta usar la empresa de usuario
            if request.user.is_authenticated and request.user.company:
                company = request.user.company

        if not company:
            return Response(
                {"detail": "No se encontró una empresa activa para este usuario."},
                status=400
            )

        serializer = self.get_serializer(company)
        return Response(serializer.data)
