from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.dateparse import parse_date

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Activity.objects.filter(created_by=user)

        # Filtro por fecha
        date_param = self.request.query_params.get('date')
        if date_param:
            try:
                date = parse_date(date_param)
                if date:
                    queryset = queryset.filter(date=date)
            except Exception as e:
                pass  # puedes agregar un manejo de error si quieres

        return queryset
