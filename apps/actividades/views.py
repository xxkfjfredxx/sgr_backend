from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.dateparse import parse_date
from datetime import datetime

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Activity.objects.filter(created_by=user)

        # Filtro por día específico (opcional)
        date_param = self.request.query_params.get('date')
        if date_param:
            try:
                date = parse_date(date_param)
                if date:
                    queryset = queryset.filter(start_date=date)
            except Exception:
                pass

        # Filtro por mes y año
        month_param = self.request.query_params.get('month')
        if month_param:
            try:
                year, month = map(int, month_param.split('-'))
                queryset = queryset.filter(
                    start_date__year=year,
                    start_date__month=month
                )
            except Exception:
                pass

        return queryset
