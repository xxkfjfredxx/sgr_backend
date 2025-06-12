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
        qs = qs.filter(employee__company=self.request.user.active_company)
        params = self.request.query_params

        if emp := params.get("employee"):
            qs = qs.filter(employee_id=emp)
        if phase := params.get("phase"):
            qs = qs.filter(exam_phase=phase)
        if et := params.get("exam_type"):  # nuevo filtro opcional
            qs = qs.filter(exam_type=et)
        if ndm := params.get("next_due_months"):  # nuevo filtro opcional
            qs = qs.filter(next_due_months=ndm)
        if f := params.get("from"):
            if d1 := parse_date(f):
                qs = qs.filter(date__gte=d1)
        if t := params.get("to"):
            if d2 := parse_date(t):
                qs = qs.filter(date__lte=d2)

        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        return Response(
            {"detail": "Examen médico restaurado."}, status=status.HTTP_200_OK
        )
