from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import Task, IPVRMatrix
from .serializers import TaskSerializer, IPVRMatrixSerializer


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class TaskViewSet(BaseAuditViewSet):
    queryset         = Task.objects.filter(is_deleted=False)
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        # ?position=<id>
        if pos := self.request.query_params.get("position"):
            qs = qs.filter(position_id=pos)
        if q := self.request.query_params.get("name"):
            qs = qs.filter(name__icontains=q)
        return qs


class IPVRMatrixViewSet(BaseAuditViewSet):
    queryset         = IPVRMatrix.objects.filter(is_deleted=False)
    serializer_class = IPVRMatrixSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        # ?task=<id>
        if task_id := self.request.query_params.get("task"):
            qs = qs.filter(task_id=task_id)
        if haz := self.request.query_params.get("hazard"):
            qs = qs.filter(hazard__icontains=haz)
        return qs
