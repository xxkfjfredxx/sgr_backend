from rest_framework import serializers
from .models import ImprovementPlan, ActionItem, RiskAction


class ActionItemSerializer(serializers.ModelSerializer):
    responsible_name = serializers.CharField(source="responsible.first_name", read_only=True)

    class Meta:
        model  = ActionItem
        fields = [
            "id", "plan", "description", "responsible", "responsible_name",
            "due_date", "completed", "evidence", "comments", "closed_at",
            "created_at", "created_by",
        ]
        read_only_fields = ("created_at", "created_by")


class ImprovementPlanSerializer(serializers.ModelSerializer):
    actions              = ActionItemSerializer(many=True, read_only=True)
    created_by_username  = serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model  = ImprovementPlan
        fields = [
            "id", "title", "description", "status",
            "created_by", "created_by_username", "created_at", "actions",
        ]
        read_only_fields = ("created_at", "created_by")


class RiskActionSerializer(serializers.ModelSerializer):
    responsible_name = serializers.CharField(source="responsible.first_name", read_only=True)
    risk_description = serializers.CharField(source="risk_assessment.hazard.description", read_only=True)

    class Meta:
        model  = RiskAction
        fields = [
            "id", "risk_assessment", "risk_description", "description",
            "responsible", "responsible_name", "due_date", "completed",
            "evidence", "comments", "closed_at", "created_at", "created_by",
        ]
        read_only_fields = ("created_at", "created_by")
