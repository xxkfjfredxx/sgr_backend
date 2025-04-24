from rest_framework import serializers
from .models import Stakeholder

class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder
        fields = '__all__'
