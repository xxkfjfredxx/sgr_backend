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
        user = self.request.user

        # 🧠 Filtro principal: actividades de la empresa del usuario
        if user.is_authenticated and hasattr(user, "employee"):
            qs = qs.filter(company=user.employee.company)

        # — ?date=YYYY-MM-DD —
        if date_str := self.request.query_params.get("date"):
            if d := parse_date(date_str):
                qs = qs.filter(start_date=d)

        # — ?month=YYYY-MM —
        if month_str := self.request.query_params.get("month"):
            try:
                year, month = map(int, month_str.split("-"))
                qs = qs.filter(start_date__year=year, start_date__month=month)
            except ValueError:
                pass

        return qs

    def perform_create(self, serializer):
        user = self.request.user
        employee = getattr(user, "employee", None)

        if employee and employee.company:
            serializer.save(created_by=user, company=employee.company)
        else:
            raise Exception("Este usuario no tiene una empresa asociada.")
