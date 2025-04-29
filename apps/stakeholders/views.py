from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from apps.utils.auditlogmimix import AuditLogMixin

from .models import Stakeholder
from .serializers import StakeholderSerializer


class StakeholderViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Stakeholder.objects.filter(is_deleted=False)
    serializer_class = StakeholderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if typ := self.request.query_params.get("type"):
            qs = qs.filter(stakeholder_type=typ)
        if act := self.request.query_params.get("active"):
            qs = qs.filter(active=act.lower() == "true")
        if before := self.request.query_params.get("contact_before"):
            if d := parse_date(before):
                qs = qs.filter(last_contact__lte=d)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response(
            {"detail": "Stakeholder restaurado."}, status=status.HTTP_200_OK
        )
