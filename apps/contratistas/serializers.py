from rest_framework import serializers
from .models import ContractorCompany, ContractorContact
from apps.empleados.models import Employee
from apps.empleados.serializers import EmployeeSerializer  # Si quieres listar empleados vinculados

class ContractorContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorContact
        fields = '__all__'

class ContractorCompanySerializer(serializers.ModelSerializer):
    contacts = ContractorContactSerializer(many=True, read_only=True)
    employees = EmployeeSerializer(many=True, read_only=True)  # Si usaste related_name='employees'

    class Meta:
        model = ContractorCompany
        fields = [
            'id', 'name', 'nit', 'address', 'phone', 'email', 'contact_person', 'active', 'created_at',
            'contacts',   # contactos vinculados (opcional)
            'employees',  # empleados vinculados (opcional)
        ]
