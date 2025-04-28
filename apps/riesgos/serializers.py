from rest_framework import serializers
from .models import Area, Hazard, RiskAssessment,RiskControl,RiskReview

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name', 'description', 'responsible']

class HazardSerializer(serializers.ModelSerializer):
    area_name = serializers.CharField(source='area.name', read_only=True)
    class Meta:
        model = Hazard
        fields = ['id', 'area', 'area_name', 'description', 'source', 'risk_type']

class RiskAssessmentSerializer(serializers.ModelSerializer):
    hazard_description = serializers.CharField(source='hazard.description', read_only=True)
    area_name = serializers.CharField(source='hazard.area.name', read_only=True)
    evaluated_by_name = serializers.CharField(source='evaluated_by.first_name', read_only=True)
    class Meta:
        model = RiskAssessment
        fields = [
            'id', 'hazard', 'hazard_description', 'area_name', 'date',
            'probability', 'severity', 'level', 'controls', 'evaluated_by',
            'evaluated_by_name', 'review_date', 'is_active'
        ]

class RiskControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskControl
        fields = '__all__'

class RiskReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskReview
        fields = '__all__'