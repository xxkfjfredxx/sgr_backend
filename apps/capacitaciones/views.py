# apps/capacitaciones/views.py
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


# ────────────────────────────────────────────────────────────────
# 1. TrainingSession  ︳ lista y detalle de sesiones
# ────────────────────────────────────────────────────────────────
class TrainingSessionViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = TrainingSession.objects.all()  # ← necesario para basename
    serializer_class = TrainingSessionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = TrainingSession.objects.all()
        qs = qs.filter(employee__company=self.request.user.active_company)
        include_deleted = self.request.query_params.get("include_deleted") == "true"
        if not include_deleted:
            qs = qs.filter(is_deleted=False)

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


# ────────────────────────────────────────────────────────────────
# 2. Attendance ︳ lista, crear, restaurar / eliminar lógico
# ────────────────────────────────────────────────────────────────
class TrainingSessionAttendanceViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = TrainingSessionAttendance.objects.all()
    serializer_class = TrainingSessionAttendanceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        • list  →  filtra is_deleted=False salvo include_deleted=true
        • detail/update/destroy → queryset completo (sin filtro)
        """
        qs = TrainingSessionAttendance.objects.all()
        qs = qs.filter(employee__company=self.request.user.active_company)
        # filtros externos
        if ses := self.request.query_params.get("session"):
            qs = qs.filter(session_id=ses)
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)

        # sólo en list ocultamos los borrados
        if self.action == "list":
            include_deleted = self.request.query_params.get("include_deleted") == "true"
            if not include_deleted:
                qs = qs.filter(is_deleted=False)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Asistencia restaurada."}, status=status.HTTP_200_OK)


# ────────────────────────────────────────────────────────────────
# 3. Certificaciones
# ────────────────────────────────────────────────────────────────
class CertificationViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = Certification.objects.all()
        qs = qs.filter(participant__employee__company=self.request.user.active_company)
        include_deleted = self.request.query_params.get("include_deleted") == "true"
        if not include_deleted:
            qs = qs.filter(is_deleted=False)

        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(participant__employee_id=emp)
        if expired := self.request.query_params.get("expired"):
            if expired.lower() == "true":
                ref = parse_date(self.request.query_params.get("ref_date", ""))
                qs = qs.filter(expiration_date__lt=ref or None)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response(
            {"detail": "Certificación restaurada."},
            status=status.HTTP_200_OK,
        )
