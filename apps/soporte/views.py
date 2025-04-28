from rest_framework import viewsets
from .models import SupportTicket, MaintenanceSchedule, MaintenanceRecord
from .serializers import SupportTicketSerializer, MaintenanceScheduleSerializer, MaintenanceRecordSerializer

class SupportTicketViewSet(viewsets.ModelViewSet):
    queryset = SupportTicket.objects.all().order_by('-created_at')
    serializer_class = SupportTicketSerializer

class MaintenanceScheduleViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceSchedule.objects.all().order_by('scheduled_date')
    serializer_class = MaintenanceScheduleSerializer

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all().order_by('-performed_date')
    serializer_class = MaintenanceRecordSerializer
