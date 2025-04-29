from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import Area, Hazard, RiskAssessment, RiskControl, RiskReview
from .serializers import (
    AreaSerializer, HazardSerializer, RiskAssessmentSerializer,
    RiskControlSerializer, RiskReviewSerializer
)


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


# -------- Áreas ---------------------------------------------------------
class AreaViewSet(BaseAuditViewSet):
    queryset         = Area.objects.filter(is_deleted=False)
    serializer_class = AreaSerializer


# -------- Peligros ------------------------------------------------------
class HazardViewSet(BaseAuditViewSet):
    queryset         = Hazard.objects.filter(is_deleted=False)
    serializer_class = HazardSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if area := self.request.query_params.get("area"):
            qs = qs.filter(area_id=area)
        if q := self.request.query_params.get("desc"):
            qs = qs.filter(description__icontains=q)
        return qs


# -------- Evaluaciones de Riesgo ----------------------------------------
class RiskAssessmentViewSet(BaseAuditViewSet):
    queryset         = RiskAssessment.objects.filter(is_deleted=False)
    serializer_class = RiskAssessmentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if haz := self.request.query_params.get("hazard"):
            qs = qs.filter(hazard_id=haz)
        if d1 := self.request.query_params.get("from"):
            if (dt := parse_date(d1)):
                qs = qs.filter(date__gte=dt)
        return qs


# -------- Controles ------------------------------------------------------
class RiskControlViewSet(BaseAuditViewSet):
    queryset         = RiskControl.objects.filter(is_deleted=False)
    serializer_class = RiskControlSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if ra := self.request.query_params.get("assessment"):
            qs = qs.filter(risk_assessment_id=ra)
        return qs


# -------- Revisiones -----------------------------------------------------
class RiskReviewViewSet(BaseAuditViewSet):
    queryset         = RiskReview.objects.filter(is_deleted=False)
    serializer_class = RiskReviewSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if ra := self.request.query_params.get("assessment"):
            qs = qs.filter(risk_assessment_id=ra)
        return qs
