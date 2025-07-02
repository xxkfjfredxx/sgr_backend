from rest_framework import serializers
from .models import Indicator, IndicatorResult


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")

    def validate_name(self, value):
        company = self.context['request'].user.company
        Model = self.Meta.model
        qs = Model.objects.filter(name=value, company=company)
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("Ya existe un registro con este nombre en tu empresa.")
        return value


class IndicatorResultSerializer(serializers.ModelSerializer):
    indicator_name = serializers.CharField(source="indicator.name", read_only=True)

    class Meta:
        model = IndicatorResult
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
