from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import ActivePauseSession, ActivePauseAttendance
from .serializers import ActivePauseSessionSerializer, ActivePauseAttendanceSerializer


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class ActivePauseSessionViewSet(BaseAuditViewSet):
    queryset = ActivePauseSession.objects.filter(is_deleted=False)
    serializer_class = ActivePauseSessionSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        # ?date=YYYY-MM-DD
        if d := self.request.query_params.get("date"):
            if dt := parse_date(d):
                qs = qs.filter(date=dt)
        # ?topic=texto
        if topic := self.request.query_params.get("topic"):
            qs = qs.filter(topic__icontains=topic)
        return qs


class ActivePauseAttendanceViewSet(BaseAuditViewSet):
    queryset = ActivePauseAttendance.objects.filter(is_deleted=False)
    serializer_class = ActivePauseAttendanceSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        # ?session=<id>
        if ses := self.request.query_params.get("session"):
            qs = qs.filter(session_id=ses)
        # ?employee=<id>
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        return qs
