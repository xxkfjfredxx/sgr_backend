from django.utils.dateparse import parse_date
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from apps.utils.auditlogmimix import AuditLogMixin

from .models import Activity
from .serializers import ActivitySerializer


class ActivityViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = Activity.objects.filter(is_deleted=False)
    serializer_class = ActivitySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()

        # Filtro por empresa vía query param
        if company_id := self.request.query_params.get("company"):
            qs = qs.filter(company_id=company_id)

        # Filtro por fecha exacta
        if date_str := self.request.query_params.get("date"):
            if d := parse_date(date_str):
                qs = qs.filter(start_date=d)

        # Filtro por mes y año
        if month_str := self.request.query_params.get("month"):
            try:
                year, month = map(int, month_str.split("-"))
                qs = qs.filter(start_date__year=year, start_date__month=month)
            except ValueError:
                pass

        return qs

    def perform_create(self, serializer):
        """
        Asigna created_by y company_id directamente desde el payload.
        No usa employmentlink_set.
        """
        user = self.request.user
        company_id = self.request.data.get("company")
        serializer.save(created_by=user, company_id=company_id)
