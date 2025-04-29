from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.utils.auditlogmimix import AuditLogMixin

from .models import ImprovementPlan, ActionItem, RiskAction
from .serializers import (
    ImprovementPlanSerializer,
    ActionItemSerializer,
    RiskActionSerializer,
)


class ImprovementPlanViewSet(AuditLogMixin, viewsets.ModelViewSet):
    """Planes de mejora (con auditoría)"""
    queryset          = ImprovementPlan.objects.filter(is_deleted=False)
    serializer_class  = ImprovementPlanSerializer
    permission_classes = [AllowAny]

    # filtro rápido ?status=open
    def get_queryset(self):
        qs = super().get_queryset()
        if st := self.request.query_params.get("status"):
            qs = qs.filter(status=st)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Plan restaurado."}, status=status.HTTP_200_OK)


class ActionItemViewSet(AuditLogMixin, viewsets.ModelViewSet):
    """Acciones específicas dentro de un plan"""
    queryset          = ActionItem.objects.filter(is_deleted=False)
    serializer_class  = ActionItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if plan := self.request.query_params.get("plan"):
            qs = qs.filter(plan_id=plan)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Acción restaurada."}, status=status.HTTP_200_OK)


class RiskActionViewSet(AuditLogMixin, viewsets.ModelViewSet):
    """Acciones derivadas de evaluación de riesgos"""
    queryset          = RiskAction.objects.filter(is_deleted=False)
    serializer_class  = RiskActionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if ass := self.request.query_params.get("risk_assessment"):
            qs = qs.filter(risk_assessment_id=ass)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Acción de riesgo restaurada."}, status=status.HTTP_200_OK)
