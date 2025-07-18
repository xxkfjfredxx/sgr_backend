from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils.dateparse import parse_date

from .models import MedicalExam
from .serializers import MedicalExamSerializer


class MedicalExamViewSet(viewsets.ModelViewSet):
    """
    API endpoints para crear, listar, filtrar y restaurar exámenes médicos.
    """

    queryset = MedicalExam.objects.filter(is_deleted=False)
    serializer_class = MedicalExamSerializer
    permission_classes = [AllowAny]

def get_queryset(self):
    qs = super().get_queryset()
    # Filtrar por la compañía activa del request, no del usuario
    active_company = getattr(self.request, "active_company", None)
    if not active_company:
        return qs.none()
    qs = qs.filter(employee__company=active_company)

    params = self.request.query_params
    # Filtro por empleado específico
    if emp := params.get("employee"):
        qs = qs.filter(employee_id=emp)
    # Filtro fase de examen
    if phase := params.get("phase"):
        qs = qs.filter(exam_phase=phase)
    # Filtro tipo de examen
    if et := params.get("exam_type"):
        qs = qs.filter(exam_type=et)
    # Próximos meses de vencimiento
    if ndm := params.get("next_due_months"):
        qs = qs.filter(next_due_months=ndm)
    # Rango de fechas
    if f := params.get("from"):
        if d1 := parse_date(f):
            qs = qs.filter(date__gte=d1)
    if t := params.get("to"):
        if d2 := parse_date(t):
            qs = qs.filter(date__lte=d2)

    return qs

@action(detail=True, methods=["post"], url_path="restore")
def restore(self, request, pk=None):
    exam = self.get_object()
    exam.is_deleted = False
    exam.save()
    return Response({"detail": "Examen médico restaurado."}, status=status.HTTP_200_OK)