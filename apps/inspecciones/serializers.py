from rest_framework import serializers
from .models import InspectionTemplate, InspectionItem, Inspection, InspectionResponse


class InspectionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionItem
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class InspectionTemplateSerializer(serializers.ModelSerializer):
    items = InspectionItemSerializer(many=True, read_only=True)

    class Meta:
        model = InspectionTemplate
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class InspectionResponseSerializer(serializers.ModelSerializer):
    item_question = serializers.CharField(source="item.question", read_only=True)

    class Meta:
        model = InspectionResponse
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class InspectionSerializer(serializers.ModelSerializer):
    responses = InspectionResponseSerializer(many=True, read_only=True)
    template_name = serializers.CharField(source="template.name", read_only=True)
    performed_by_name = serializers.CharField(
        source="performed_by.first_name", read_only=True
    )

    class Meta:
        model = Inspection
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
