from rest_framework import serializers
from .models import Task, IPVRMatrix


class TaskSerializer(serializers.ModelSerializer):
    position_name = serializers.CharField(source="position.name", read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")


class IPVRMatrixSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source="task.name", read_only=True)

    class Meta:
        model = IPVRMatrix
        fields = "__all__"
        read_only_fields = ("created_at", "created_by")
