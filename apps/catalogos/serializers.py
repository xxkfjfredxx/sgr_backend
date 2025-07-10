from rest_framework import serializers
from .models import Branch, Position, WorkArea


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ['company']
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


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        exclude = ['company']
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


class WorkAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArea
        exclude = ['company']
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
