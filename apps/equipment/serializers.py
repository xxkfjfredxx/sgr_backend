from rest_framework import serializers
from .models import EquipmentInventory, EquipmentInspection


class EquipmentInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentInventory
        fields = [
            "id",
            "company",
            "categoria",
            "serial",
            "cantidad",  # nuevo
            "fecha_compra",
            "certificado",
            "estado",
        ]
        read_only_fields = ["id"]


class EquipmentInspectionSerializer(serializers.ModelSerializer):
    equipment_data = EquipmentInventorySerializer(source="equipment", read_only=True)

    class Meta:
        model = EquipmentInspection
        fields = [
            "id",
            "equipment",
            "equipment_data",
            "fecha",
            "resultado",
            "tecnico",
            "evidencia",
        ]
        read_only_fields = ["id"]
