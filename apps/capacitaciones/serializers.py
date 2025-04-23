from rest_framework import serializers
from .models import TrainingSession, TrainingSessionAttendance

class TrainingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSession
        fields = '__all__'

class TrainingSessionAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSessionAttendance
        fields = '__all__'
