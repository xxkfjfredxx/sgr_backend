from rest_framework import serializers
from .models import EmploymentLink


class EmploymentLinkSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.first_name", read_only=True)
    company_name = serializers.CharField(source="company.name", read_only=True)

    class Meta:
        model = EmploymentLink
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
