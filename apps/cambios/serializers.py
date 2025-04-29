from rest_framework import serializers
from .models import ChangeRequest, ChangeEvaluation, ChangeImplementation


class ChangeRequestSerializer(serializers.ModelSerializer):
    requested_by_username = serializers.CharField(source="requested_by.username", read_only=True)

    class Meta:
        model  = ChangeRequest
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class ChangeEvaluationSerializer(serializers.ModelSerializer):
    evaluated_by_username = serializers.CharField(source="evaluated_by.username", read_only=True)

    class Meta:
        model  = ChangeEvaluation
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class ChangeImplementationSerializer(serializers.ModelSerializer):
    implemented_by_name  = serializers.CharField(source="implemented_by.first_name", read_only=True)
    verified_by_username = serializers.CharField(source="verified_by.username", read_only=True)

    class Meta:
        model  = ChangeImplementation
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
