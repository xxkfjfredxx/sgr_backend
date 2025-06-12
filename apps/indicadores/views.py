# apps/indicadores/views.py

from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import FloatField, F, ExpressionWrapper, Sum
from django.db.models.functions import Cast
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.permissions import AllowAny

from apps.utils.auditlogmimix import AuditLogMixin
from .models import Indicator, IndicatorResult
from .serializers import IndicatorSerializer, IndicatorResultSerializer

from apps.ausentismo.models import Absence
from apps.capacitaciones.models import TrainingSession, TrainingSessionAttendance
from apps.seguridad_industrial.models import WorkAccident
from apps.salud_ocupacional.models import MedicalExam
from apps.empleados.models import Employee


class BaseAuditViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class IndicatorViewSet(BaseAuditViewSet):
    queryset = Indicator.objects.filter(is_deleted=False)
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if name := self.request.query_params.get("name"):
            qs = qs.filter(name__icontains=name)
        return qs


class IndicatorResultViewSet(BaseAuditViewSet):
    queryset = IndicatorResult.objects.filter(is_deleted=False)
    serializer_class = IndicatorResultSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if ind := self.request.query_params.get("indicator"):
            qs = qs.filter(indicator_id=ind)
        if per := self.request.query_params.get("period"):
            qs = qs.filter(period=per)
        return qs


@api_view(["GET"])
def indicator_summary(request):
    """
    Devuelve % de ausentismo, capacitación, accidentes y aptitud
    en un rango YYYY-MM → YYYY-MM (inclusive).
    Ejemplo: /api/indicator-summary?company=1&from=2025-01&to=2025-12
    """
    # parsear fechas de parámetro
    try:
        from_date = (
            datetime.strptime(request.GET.get("from"), "%Y-%m").date().replace(day=1)
        )
        to_date = (
            datetime.strptime(request.GET.get("to"), "%Y-%m").date().replace(day=1)
        )
    except Exception:
        return Response(
            {"error": "Formato inválido. Usa YYYY-MM en 'from' y 'to'."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # calcular último día de mes to_date
    last_day = (to_date.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(
        days=1
    )

    # --- AUSENTISMO ---
    absences = Absence.objects.filter(
        start_date__lte=last_day, end_date__gte=from_date
    ).annotate(
        days=ExpressionWrapper(
            Cast(F("end_date"), FloatField()) - Cast(F("start_date"), FloatField()) + 1,
            output_field=FloatField(),
        )
    )
    total_days_absent = absences.aggregate(total=Sum("days"))["total"] or 0

    total_employees = Employee.objects.count()
    total_days_worked = total_employees * ((last_day - from_date).days + 1)
    absenteeism_percent = (
        round((total_days_absent / total_days_worked) * 100, 2)
        if total_days_worked
        else 0
    )

    # --- CAPACITACIÓN ---
    sessions = TrainingSession.objects.filter(date__range=(from_date, last_day)).count()
    attendances = TrainingSessionAttendance.objects.filter(
        session__date__range=(from_date, last_day), attended=True
    ).count()
    training_completion_percent = round((attendances / (total_employees or 1)) * 100, 2)

    # --- ACCIDENTES ---
    accident_count = WorkAccident.objects.filter(
        date__range=(from_date, last_day)
    ).count()
    accident_rate = round((accident_count / (total_employees or 1)) * 100, 2)

    # --- APTITUD MÉDICA (basado en next_due ya calculado) ---
    company_id = request.GET.get("company")
    today = timezone.localdate()
    threshold = today + timedelta(days=30)

    qs = MedicalExam.objects.filter(
        company_id=company_id, date__range=(from_date, last_day)
    ).exclude(next_due__isnull=True)

    total_exams = qs.count()
    valid = expiring = expired = 0

    for e in qs:
        nd = e.next_due
        if nd > threshold:
            valid += 1
        elif nd > today:
            expiring += 1
        else:
            expired += 1

    aptitude_percent = round((valid / (total_exams or 1)) * 100, 2)

    return Response(
        {
            "range": f"{from_date:%Y-%m} → {to_date:%Y-%m}",
            "absenteeism_percent": absenteeism_percent,
            "training_completion_percent": training_completion_percent,
            "accident_rate": accident_rate,
            "aptitude_percent": aptitude_percent,
            "total_sessions": sessions,
            "total_accidents": accident_count,
            "total_medical_exams": total_exams,
            "aptitude": {
                "total": total_exams,
                "valid": valid,
                "expiring": expiring,
                "expired": expired,
            },
        }
    )
