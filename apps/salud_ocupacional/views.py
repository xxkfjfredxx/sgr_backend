from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import MedicalExam
from .serializers import MedicalExamSerializer


class MedicalExamViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset           = MedicalExam.objects.filter(is_deleted=False)
    serializer_class   = MedicalExamSerializer
    permission_classes = [AllowAny]

    # ---------- filtros rápidos ----------
    def get_queryset(self):
        qs = super().get_queryset()

        # ?employee=<id>
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)

        # ?type=Ingreso/Periódico/Retiro
        if t := self.request.query_params.get("type"):
            qs = qs.filter(exam_type=t)

        # ?from=YYYY-MM-DD  |  ?to=YYYY-MM-DD
        if f := self.request.query_params.get("from"):
            if (d1 := parse_date(f)):
                qs = qs.filter(date__gte=d1)
        if t := self.request.query_params.get("to"):
            if (d2 := parse_date(t)):
                qs = qs.filter(date__lte=d2)

        return qs

    # ---------- restaurar lógico ----------
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Examen médico restaurado."}, status=status.HTTP_200_OK)
