from django.utils.dateparse import parse_date
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import InspectionTemplate, InspectionItem, Inspection, InspectionResponse
from .serializers import (
    InspectionTemplateSerializer,
    InspectionItemSerializer,
    InspectionSerializer,
    InspectionResponseSerializer,
)


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


# ---------------- Templates & Items -----------------
class InspectionTemplateViewSet(BaseAuditViewSet):
    queryset = InspectionTemplate.objects.filter(is_deleted=False)
    serializer_class = InspectionTemplateSerializer


class InspectionItemViewSet(BaseAuditViewSet):
    queryset = InspectionItem.objects.filter(is_deleted=False)
    serializer_class = InspectionItemSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if tmpl := self.request.query_params.get("template"):
            qs = qs.filter(template_id=tmpl)
        return qs


# ---------------- Inspections -----------------------
class InspectionViewSet(BaseAuditViewSet):
    queryset = Inspection.objects.filter(is_deleted=False)
    serializer_class = InspectionSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(employee__company=self.request.user.active_company)
        if tmpl := self.request.query_params.get("template"):
            qs = qs.filter(template_id=tmpl)
        if emp := self.request.query_params.get("performed_by"):
            qs = qs.filter(performed_by_id=emp)
        if d := self.request.query_params.get("date"):
            if dt := parse_date(d):
                qs = qs.filter(date=dt)
        return qs


# ---------------- Responses -------------------------
class InspectionResponseViewSet(BaseAuditViewSet):
    queryset = InspectionResponse.objects.filter(is_deleted=False)
    serializer_class = InspectionResponseSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(inspection__employee__company=self.request.user.active_company)

        if insp := self.request.query_params.get("inspection"):
            qs = qs.filter(inspection_id=insp)
        if item := self.request.query_params.get("item"):
            qs = qs.filter(item_id=item)
        return qs
