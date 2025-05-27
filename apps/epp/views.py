from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import EPPItem, EPPAssignment
from .serializers import EPPItemSerializer, EPPAssignmentSerializer


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class EPPItemViewSet(BaseAuditViewSet):
    queryset = EPPItem.objects.filter(is_deleted=False)
    serializer_class = EPPItemSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if name := self.request.query_params.get("name"):
            qs = qs.filter(name__icontains=name)
        return qs


class EPPAssignmentViewSet(BaseAuditViewSet):
    queryset = EPPAssignment.objects.filter(is_deleted=False)
    serializer_class = EPPAssignmentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(employee__company=self.request.user.active_company)
        if emp := self.request.query_params.get("employee"):
            qs = qs.filter(employee_id=emp)
        if item := self.request.query_params.get("item"):
            qs = qs.filter(epp_item_id=item)
        if act := self.request.query_params.get("active"):
            qs = qs.filter(is_active=act.lower() == "true")
        return qs
