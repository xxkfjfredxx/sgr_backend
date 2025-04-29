from rest_framework import serializers
from .models import ErgonomicAssessment, ARO, ATS


class ErgonomicAssessmentSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)
    position_name = serializers.CharField(source="position.name",      read_only=True)

    class Meta:
        model  = ErgonomicAssessment
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class AROSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)
    position_name = serializers.CharField(source="position.name",      read_only=True)

    class Meta:
        model  = ARO
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class ATSSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)
    position_name = serializers.CharField(source="position.name",      read_only=True)

    class Meta:
        model  = ATS
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
