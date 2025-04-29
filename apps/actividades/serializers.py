from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(
        source="created_by.username", read_only=True
    )

    class Meta:
        model = Activity
        fields = "__all__"
        read_only_fields = ("is_deleted", "created_at", "created_by", "updated_at")
