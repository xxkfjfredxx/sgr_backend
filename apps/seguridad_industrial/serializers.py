from rest_framework import serializers
from .models import WorkAccident, WorkAtHeightPermit
from apps.empleados.serializers import EmployeeSerializer


class WorkAccidentSerializer(serializers.ModelSerializer):
    # datos de empleado para mostrar en la lista
    employee_data = EmployeeSerializer(source="employee", read_only=True)

    class Meta:
        model = WorkAccident
        fields = [
            "id",
            "employee",
            "employee_data",
            "company",
            "incident_type",
            "date",
            "location",
            "description",
            "injury_type",
            "severity",
            "reported_to_arl",
            "days_lost",
            "training_valid",
            "medical_exam_valid",
            "corrective_actions",
            "evidence_file",
            "created_by",
            "created_at",
            "updated_at",
            "is_deleted",
        ]
        read_only_fields = (
            "id",
            "employee_data",
            "created_by",
            "created_at",
            "updated_at",
            "is_deleted",
        )


class WorkAtHeightPermitSerializer(serializers.ModelSerializer):
    employee_data = EmployeeSerializer(source="employee", read_only=True)

    class Meta:
        model = WorkAtHeightPermit
        fields = [
            "id",
            "employee",
            "employee_data",
            "date",
            "location",
            "work_description",
            "checklist",
            "approved",
            "supervisor",
            "evidence_file",
            "created_by",
            "created_at",
            "updated_at",
            "is_deleted",
        ]
        read_only_fields = (
            "id",
            "employee_data",
            "created_by",
            "created_at",
            "updated_at",
            "is_deleted",
        )
