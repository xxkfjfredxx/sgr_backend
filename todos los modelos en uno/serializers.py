from rest_framework import serializers
from .models import (
    UserRole, User, Branch, Position, WorkArea, DocumentType, Employee,
    EmploymentLink, PersonalDocument, WorkHistory, SystemAudit
)

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class WorkAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArea
        fields = '__all__'

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmploymentLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentLink
        fields = '__all__'

class PersonalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDocument
        fields = '__all__'

class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = '__all__'

class SystemAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAudit
        fields = '__all__'

