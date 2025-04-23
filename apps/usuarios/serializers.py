from rest_framework import serializers
from apps.empleados.models import Employee
from .models import (
    UserRole, User
)

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    employee_id = serializers.SerializerMethodField()

    def get_employee_id(self, obj):
        # Si la relación es OneToOneField desde Employee a User:
        try:
            return obj.employee.id  # Ajusta esto según tu relación
        except Employee.DoesNotExist:
            return None

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'is_superuser', 'is_staff', 'role',
            'employee_id',  # <-- aquí
        ]