from rest_framework import serializers
from .models import Indicator, IndicatorResult

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'

class IndicatorResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicatorResult
        fields = '__all__'
