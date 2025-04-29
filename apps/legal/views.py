from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import LegalRequirement
from .serializers import LegalRequirementSerializer


class LegalRequirementViewSet(AuditLogMixin, viewsets.ModelViewSet):
    """
    CRUD de requisitos legales con auditoría y borrado lógico.
    """

    queryset = LegalRequirement.objects.filter(is_deleted=False)
    serializer_class = LegalRequirementSerializer
    permission_classes = [AllowAny]

    # ------------- filtros rápidos --------------
    def get_queryset(self):
        qs = super().get_queryset()

        # ?area=<id>
        if area := self.request.query_params.get("area"):
            qs = qs.filter(area_id=area)

        # ?active=true/false
        if act := self.request.query_params.get("active"):
            qs = qs.filter(active=act.lower() == "true")

        # ?expires_before=YYYY-MM-DD
        if exp := self.request.query_params.get("expires_before"):
            if dt := parse_date(exp):
                qs = qs.filter(expiration_date__lte=dt)

        return qs

    # ------------- restaurar registro -----------
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response(
            {"detail": "Requisito legal restaurado."}, status=status.HTTP_200_OK
        )
