from rest_framework import serializers
from .models import Employee, EmployeeDocument, DocumentType


class EmployeeSerializer(serializers.ModelSerializer):
    # Campo extra para el email del usuario relacionado
    user_email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Employee
        # Incluimos todos los campos del modelo + el extra user_email
        fields = "__all__"
        read_only_fields = ("created_at", "created_by", "user_email")


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
