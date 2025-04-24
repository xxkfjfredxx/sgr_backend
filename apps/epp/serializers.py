from rest_framework import serializers
from .models import EPPItem, EPPAssignment

class EPPItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EPPItem
        fields = ['id', 'name', 'description', 'stock', 'expiration_date']

class EPPAssignmentSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)
    epp_item_name = serializers.CharField(source="epp_item.name", read_only=True)

    class Meta:
        model = EPPAssignment
        fields = [
            'id', 'employee', 'employee_name', 'epp_item', 'epp_item_name',
            'assigned_at', 'returned_at', 'condition_on_return', 'assigned_by',
            'evidence', 'is_active'
        ]
