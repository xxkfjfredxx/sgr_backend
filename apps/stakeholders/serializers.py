from rest_framework import serializers
from .models import Stakeholder


class StakeholderSerializer(serializers.ModelSerializer):
    work_area_name = serializers.CharField(source="work_area.name", read_only=True)

    class Meta:
        model = Stakeholder
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
