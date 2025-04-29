from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.utils.auditlogmimix import AuditLogMixin

from .models import ErgonomicAssessment, ARO, ATS
from .serializers import ErgonomicAssessmentSerializer, AROSerializer, ATSSerializer


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


# --------- ErgonomicAssessment -------------
class ErgonomicAssessmentViewSet(BaseAuditViewSet):
    queryset         = ErgonomicAssessment.objects.filter(is_deleted=False)
    serializer_class = ErgonomicAssessmentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        if date_str := self.request.query_params.get("date"):
            if (d := parse_date(date_str)):
                qs = qs.filter(date=d)
        return qs


# ---------------- ARO ----------------------
class AROViewSet(BaseAuditViewSet):
    queryset         = ARO.objects.filter(is_deleted=False)
    serializer_class = AROSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if hazard := self.request.query_params.get("hazard"):
            qs = qs.filter(hazard__icontains=hazard)
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        return qs


# ---------------- ATS ----------------------
class ATSViewSet(BaseAuditViewSet):
    queryset         = ATS.objects.filter(is_deleted=False)
    serializer_class = ATSSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if activity := self.request.query_params.get("activity"):
            qs = qs.filter(activity__icontains=activity)
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        return qs
