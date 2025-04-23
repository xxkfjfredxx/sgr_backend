from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Count, Sum, Q
from datetime import datetime

from .models import Indicator, IndicatorResult
from .serializers import IndicatorSerializer, IndicatorResultSerializer

from apps.ausentismo.models import Absence
from apps.capacitaciones.models import TrainingSession, TrainingSessionAttendance
from apps.seguridad_industrial.models import WorkAccident
from apps.salud_ocupacional.models import MedicalExam
from apps.empleados.models import Employee


class IndicatorViewSet(viewsets.ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    permission_classes = [AllowAny]


class IndicatorResultViewSet(viewsets.ModelViewSet):
    queryset = IndicatorResult.objects.all()
    serializer_class = IndicatorResultSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
def indicator_summary(request):
    print("💡 Entró al summary")
    from_date = request.GET.get('from')  # formato esperado: '2024-01'
    to_date = request.GET.get('to')      # formato esperado: '2024-12'

    # Parse fechas inicial y final
    try:
        from_date = datetime.strptime(from_date, '%Y-%m')
        to_date = datetime.strptime(to_date, '%Y-%m')
    except:
        return Response({"error": "Formato de fecha inválido. Usa YYYY-MM."}, status=400)

    # Filtro por rango
    date_filter = Q(start_date__gte=from_date, start_date__lte=to_date)

    # === AUSENTISMO ===
    total_absences = Absence.objects.filter(date_filter).aggregate(dias=Sum('end_date')) or {}
    dias_ausencia = total_absences.get('dias') or 0

    total_empleados = Employee.objects.count()
    dias_trabajados = total_empleados * 30  # Suponiendo 30 días por mes

    absenteeism_percent = round((dias_ausencia / dias_trabajados) * 100, 2) if dias_trabajados else 0

    # === CAPACITACIÓN ===
    total_sessions = TrainingSession.objects.filter(date__gte=from_date, date__lte=to_date).count()
    total_asistencias = TrainingSessionAttendance.objects.filter(
        session__date__gte=from_date, session__date__lte=to_date, attended=True
    ).count()

    training_completion_percent = round((total_asistencias / (total_empleados or 1)) * 100, 2)

    # === ACCIDENTES ===
    accident_count = WorkAccident.objects.filter(date__gte=from_date, date__lte=to_date).count()
    accident_rate = round((accident_count / (total_empleados or 1)) * 100, 2)

    # === APTITUD MÉDICA ===
    aptos = MedicalExam.objects.filter(
        date__gte=from_date, date__lte=to_date, aptitude__icontains='apto'
    ).count()
    evaluados = MedicalExam.objects.filter(
        date__gte=from_date, date__lte=to_date
    ).count()
    aptitude_percent = round((aptos / (evaluados or 1)) * 100, 2)

    return Response({
        "absenteeism_percent": absenteeism_percent,
        "training_completion_percent": training_completion_percent,
        "accident_rate": accident_rate,
        "aptitude_percent": aptitude_percent,
    })
