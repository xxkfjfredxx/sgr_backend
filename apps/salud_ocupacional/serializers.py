from rest_framework import serializers
from .models import MedicalExam


class MedicalExamSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)

    class Meta:
        model  = MedicalExam
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
