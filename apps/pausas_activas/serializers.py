from rest_framework import serializers
from .models import ActivePauseSession, ActivePauseAttendance
from apps.empleados.models import Employee
from apps.empleados.serializers import EmployeeSerializer

class ActivePauseAttendanceSerializer(serializers.ModelSerializer):
    employee_data = EmployeeSerializer(source='employee', read_only=True)
    
    class Meta:
        model = ActivePauseAttendance
        fields = ['id', 'session', 'employee', 'employee_data', 'attended', 'signature']

class ActivePauseSessionSerializer(serializers.ModelSerializer):
    attendances = ActivePauseAttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = ActivePauseSession
        fields = ['id', 'date', 'topic', 'facilitator', 'comments', 'created_at', 'attendances']
