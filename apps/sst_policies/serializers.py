from rest_framework import serializers
from .models import SSTPolicy, PolicyAcceptance

class SSTPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = SSTPolicy
        fields = '__all__'

class PolicyAcceptanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyAcceptance
        fields = '__all__'
