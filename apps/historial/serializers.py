from rest_framework import serializers
from .models import WorkHistory


class WorkHistorySerializer(serializers.ModelSerializer):
    employment_link_id = serializers.IntegerField(source="employment_link.id", read_only=True)
    changed_by_username = serializers.CharField(source="changed_by.username", read_only=True)

    class Meta:
        model  = WorkHistory
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
