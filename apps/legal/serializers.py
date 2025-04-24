from rest_framework import serializers
from .models import LegalRequirement

class LegalRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalRequirement
        fields = '__all__'
