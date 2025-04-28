from rest_framework import serializers
from .models import ChangeRequest, ChangeEvaluation, ChangeImplementation

class ChangeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeRequest
        fields = '__all__'

class ChangeEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeEvaluation
        fields = '__all__'

class ChangeImplementationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeImplementation
        fields = '__all__'
