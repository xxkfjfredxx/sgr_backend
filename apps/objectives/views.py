from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import SSTObjective, SSTGoal
from .serializers import SSTObjectiveSerializer, SSTGoalSerializer


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


# ---------------- Objectives ----------------
class SSTObjectiveViewSet(BaseAuditViewSet):
    queryset         = SSTObjective.objects.filter(is_deleted=False)
    serializer_class = SSTObjectiveSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if res := self.request.query_params.get("responsible"):
            qs = qs.filter(responsible_id=res)
        if st := self.request.query_params.get("status"):
            qs = qs.filter(status=st)
        if d := self.request.query_params.get("due_before"):
            if (dt := parse_date(d)):
                qs = qs.filter(due_date__lte=dt)
        return qs


# ---------------- Goals ---------------------
class SSTGoalViewSet(BaseAuditViewSet):
    queryset         = SSTGoal.objects.filter(is_deleted=False)
    serializer_class = SSTGoalSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if obj := self.request.query_params.get("objective"):
            qs = qs.filter(objective_id=obj)
        if st := self.request.query_params.get("status"):
            qs = qs.filter(status=st)
        return qs
