from rest_framework import serializers
from .models import Reintegro
from apps.empleados.serializers import EmployeeSerializer

class ReintegroSerializer(serializers.ModelSerializer):
    employee_data = EmployeeSerializer(source='employee', read_only=True)

    class Meta:
        model = Reintegro
        fields = [
            'id', 'employee', 'employee_data',
            'start_date', 'end_date', 'medical_recommendations',
            'position_modification', 'workplace_adaptation',
            'observations', 'successful', 'created_at'
        ]
