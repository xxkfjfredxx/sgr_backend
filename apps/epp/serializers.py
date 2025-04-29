from rest_framework import serializers
from .models import EPPItem, EPPAssignment


class EPPItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EPPItem
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class EPPAssignmentSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)
    epp_item_name = serializers.CharField(source="epp_item.name",   read_only=True)

    class Meta:
        model  = EPPAssignment
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
