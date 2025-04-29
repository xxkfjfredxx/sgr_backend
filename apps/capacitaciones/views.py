from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.utils.auditlogmimix import AuditLogMixin

from .models import TrainingSession, TrainingSessionAttendance, Certification
from .serializers import (
    TrainingSessionSerializer,
    TrainingSessionAttendanceSerializer,
    CertificationSerializer,
)


class TrainingSessionViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = TrainingSession.objects.filter(is_deleted=False)
    serializer_class = TrainingSessionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if topic := self.request.query_params.get("topic"):
            qs = qs.filter(topic__icontains=topic)
        if date_str := self.request.query_params.get("date"):
            if d := parse_date(date_str):
                qs = qs.filter(date=d)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Sesión restaurada."}, status=status.HTTP_200_OK)


class TrainingSessionAttendanceViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = TrainingSessionAttendance.objects.filter(is_deleted=False)
    serializer_class = TrainingSessionAttendanceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if ses := self.request.query_params.get("session"):
            qs = qs.filter(session_id=ses)
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Asistencia restaurada."}, status=status.HTTP_200_OK)


class CertificationViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Certification.objects.filter(is_deleted=False)
    serializer_class = CertificationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(participant__employee_id=emp)
        if expired := self.request.query_params.get("expired"):
            if expired.lower() == "true":
                qs = qs.filter(
                    expiration_date__lt=parse_date(
                        self.request.query_params.get("ref_date", "")
                    )
                    or None
                )
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response(
            {"detail": "Certificación restaurada."}, status=status.HTTP_200_OK
        )
