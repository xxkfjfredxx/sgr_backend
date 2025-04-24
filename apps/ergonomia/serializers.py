from rest_framework import serializers
from .models import ErgonomicAssessment, ARO, ATS
from apps.empleados.models import Employee
from apps.catalogos.models import Position

class ErgonomicAssessmentSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.first_name', read_only=True)
    position_name = serializers.CharField(source='position.name', read_only=True)

    class Meta:
        model = ErgonomicAssessment
        fields = [
            'id', 'employee', 'employee_name', 'position', 'position_name',
            'area', 'date', 'evaluation_type', 'summary', 'file', 'responsible', 'created_at'
        ]

class AROSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.first_name', read_only=True)
    position_name = serializers.CharField(source='position.name', read_only=True)

    class Meta:
        model = ARO
        fields = [
            'id', 'employee', 'employee_name', 'position', 'position_name',
            'date', 'description', 'hazard', 'risk', 'control', 'evidence', 'created_at'
        ]

class ATSSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.first_name', read_only=True)
    position_name = serializers.CharField(source='position.name', read_only=True)

    class Meta:
        model = ATS
        fields = [
            'id', 'employee', 'employee_name', 'position', 'position_name',
            'date', 'activity', 'hazard', 'risk', 'control', 'evidence', 'created_at'
        ]
