from rest_framework import serializers
from .models import SignageInventory, VaccinationRecord


class SignageInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SignageInventory
        fields = [
            "id",
            "company",
            "tipo_senal",
            "ubicacion_plano",
            "photo",
            "installed_at",
        ]


class VaccinationRecordSerializer(serializers.ModelSerializer):
    # campos solo lectura para mostrar nombre y cédula
    employee_name = serializers.CharField(source="employee.full_name", read_only=True)
    employee_document = serializers.CharField(
        source="employee.document", read_only=True
    )

    class Meta:
        model = VaccinationRecord
        fields = [
            "id",
            "employee",  # pk para creación/actualización
            "employee_name",  # solo lectura
            "employee_document",  # solo lectura
            "vacuna",
            "fecha",
            "fecha_vencimiento",
            "soporte",
        ]
        read_only_fields = ["id", "employee_name", "employee_document"]
