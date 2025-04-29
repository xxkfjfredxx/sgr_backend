from rest_framework import viewsets
from rest_framework.permissions import (
    AllowAny,
)  # cámbialo a IsAuthenticated cuando quieras
from .models import WorkHistory
from .serializers import WorkHistorySerializer


class WorkHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Histórico inmutable de cambios en EmploymentLink.
    Solo lectura (GET list / retrieve).
    """

    queryset = WorkHistory.objects.all()  # ya está ordenado desde Meta
    serializer_class = WorkHistorySerializer
    permission_classes = [AllowAny]

    # ----- filtros rápidos -----
    def get_queryset(self):
        qs = super().get_queryset()

        if link_id := self.request.query_params.get("employment_link"):
            qs = qs.filter(employment_link_id=link_id)

        if field := self.request.query_params.get("field"):
            qs = qs.filter(modified_field__icontains=field)

        return qs
