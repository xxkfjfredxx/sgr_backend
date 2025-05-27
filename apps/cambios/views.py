from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.utils.auditlogmimix import AuditLogMixin

from .models import ChangeRequest, ChangeEvaluation, ChangeImplementation
from .serializers import (
    ChangeRequestSerializer,
    ChangeEvaluationSerializer,
    ChangeImplementationSerializer,
)


class ChangeRequestViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = ChangeRequest.objects.filter(is_deleted=False)
    serializer_class = ChangeRequestSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(employee__company=self.request.user.active_company)
        if st := self.request.query_params.get("status"):
            qs = qs.filter(status=st)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Solicitud restaurada."}, status=status.HTTP_200_OK)


class ChangeEvaluationViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = ChangeEvaluation.objects.filter(is_deleted=False)
    serializer_class = ChangeEvaluationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(employee__company=self.request.user.active_company)
        if risk := self.request.query_params.get("risk"):
            qs = qs.filter(risk_level=risk)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Evaluación restaurada."}, status=status.HTTP_200_OK)


class ChangeImplementationViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = ChangeImplementation.objects.filter(is_deleted=False)
    serializer_class = ChangeImplementationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(employee__company=self.request.user.active_company)
        if impl := self.request.query_params.get("implemented_by"):
            qs = qs.filter(implemented_by_id=impl)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response(
            {"detail": "Implementación restaurada."}, status=status.HTTP_200_OK
        )
