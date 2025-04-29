from rest_framework import serializers
from .models import Employee, EmployeeDocument, DocumentType


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class EmployeeDocumentSerializer(serializers.ModelSerializer):
    document_type_name = serializers.CharField(
        source="document_type.name", read_only=True
    )
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)

    class Meta:
        model = EmployeeDocument
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
