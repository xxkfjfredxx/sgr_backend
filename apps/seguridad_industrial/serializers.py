from rest_framework import serializers
from .models import WorkAccident

class WorkAccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkAccident
        fields = '__all__'
