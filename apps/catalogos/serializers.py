from rest_framework import serializers
from .models import Branch, Position, WorkArea


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Branch
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Position
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class WorkAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = WorkArea
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
