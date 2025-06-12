from rest_framework import serializers
from .models import MedicalExam


class MedicalExamSerializer(serializers.ModelSerializer):
    # employee_name = serializers.CharField(source="employee.first_name", read_only=True)

    class Meta:
        model = MedicalExam
        fields = [
            "id",
            "employee",
            "company",
            "exam_phase",
            "exam_type",  # antes sub_type
            "date",
            "entity_ips",  # antes entity
            "aptitude",
            "recommendations",
            "file",
            "next_due_months",
            "next_due",
            "metrics",
        ]
        read_only_fields = ("next_due", "created_at", "created_by", "updated_at")
