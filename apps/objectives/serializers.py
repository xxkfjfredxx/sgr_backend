from rest_framework import serializers
from .models import SSTObjective, SSTGoal


class SSTGoalSerializer(serializers.ModelSerializer):
    objective_title = serializers.CharField(source="objective.title", read_only=True)

    class Meta:
        model  = SSTGoal
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class SSTObjectiveSerializer(serializers.ModelSerializer):
    goals            = SSTGoalSerializer(many=True, read_only=True)
    responsible_name = serializers.CharField(source="responsible.username", read_only=True)

    class Meta:
        model  = SSTObjective
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
