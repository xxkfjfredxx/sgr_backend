from rest_framework import serializers
from .models import Task, IPVRMatrix
from apps.catalogos.models import Position  # Asumiendo que ya tienes este modelo

class TaskSerializer(serializers.ModelSerializer):
    position_name = serializers.CharField(source='position.name', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'position', 'position_name', 'active', 'created_at']

class IPVRMatrixSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source='task.name', read_only=True)

    class Meta:
        model = IPVRMatrix
        fields = [
            'id', 'task', 'task_name', 'hazard', 'risk', 'control',
            'severity', 'probability', 'evaluation', 'created_at'
        ]
