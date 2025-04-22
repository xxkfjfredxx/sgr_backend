from rest_framework import serializers
from apps.empleados.models import Employee, EmployeeDocument
from apps.empleados.models import DocumentType # ✅ correcto aquí

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class EmployeeDocumentSerializer(serializers.ModelSerializer):
    document_type_name = serializers.CharField(source='document_type.name', read_only=True)

    class Meta:
        model = EmployeeDocument
        fields = ['id', 'employee', 'document_type', 'document_type_name', 'file', 'uploaded_at']
