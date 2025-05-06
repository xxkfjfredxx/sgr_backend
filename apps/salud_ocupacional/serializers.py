from rest_framework import serializers
from .models import MedicalExam


class MedicalExamSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)

    class Meta:
        model = MedicalExam
        fields = [
            "id",
            "employee",
            "employee_name",
            "company",
            "exam_phase",
            "sub_type",
            "risk_level",
            "date",
            "entity",
            "aptitude",
            "recommendations",
            "file",
            "metrics",
            "next_due",
            "created_at",
            "created_by",
            "updated_at",
        ]
        read_only_fields = ("created_at", "created_by", "updated_at")
