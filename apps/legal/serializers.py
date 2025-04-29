from rest_framework import serializers
from .models import LegalRequirement


class LegalRequirementSerializer(serializers.ModelSerializer):
    area_name = serializers.CharField(source="area.name", read_only=True)

    class Meta:
        model = LegalRequirement
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
