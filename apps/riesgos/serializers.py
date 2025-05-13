from rest_framework import serializers
from .models import (
    Area,
    Hazard,
    RiskAssessment,
    RiskControl,
    RiskReview,
    ControlEvidence,
    ControlFollowUp,
)


class AreaSerializer(serializers.ModelSerializer):
    responsible_name = serializers.CharField(
        source="responsible.first_name", read_only=True
    )

    class Meta:
        model = Area
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class HazardSerializer(serializers.ModelSerializer):
    area_name = serializers.CharField(source="area.name", read_only=True)

    class Meta:
        model = Hazard
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class RiskAssessmentSerializer(serializers.ModelSerializer):
    hazard_description = serializers.CharField(
        source="hazard.description", read_only=True
    )
    area_name = serializers.CharField(source="hazard.area.name", read_only=True)
    evaluated_by_name = serializers.CharField(
        source="evaluated_by.first_name", read_only=True
    )

    class Meta:
        model = RiskAssessment
        fields = "__all__"
        read_only_fields = ("created_at", "created_by", "level")


class RiskControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskControl
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class ControlEvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlEvidence
        fields = "__all__"
        read_only_fields = ("uploaded_at",)


class ControlFollowUpSerializer(serializers.ModelSerializer):
    performed_by_name = serializers.CharField(
        source="performed_by.first_name", read_only=True
    )

    class Meta:
        model = ControlFollowUp
        fields = "__all__"
        read_only_fields = ("date",)


class RiskReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskReview
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
