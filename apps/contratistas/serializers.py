from rest_framework import serializers
from .models import ContractorCompany, ContractorContact
from apps.empleados.serializers import EmployeeSerializer   # opcional


class ContractorContactSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ContractorContact
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class ContractorCompanySerializer(serializers.ModelSerializer):
    contacts  = ContractorContactSerializer(many=True, read_only=True)
    employees = EmployeeSerializer(many=True, read_only=True)  # si definiste related_name="employees"

    class Meta:
        model  = ContractorCompany
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
