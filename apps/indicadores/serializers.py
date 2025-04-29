from rest_framework import serializers
from .models import Indicator, IndicatorResult


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class IndicatorResultSerializer(serializers.ModelSerializer):
    indicator_name = serializers.CharField(source="indicator.name", read_only=True)

    class Meta:
        model = IndicatorResult
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
