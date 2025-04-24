from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Task, IPVRMatrix
from .serializers import TaskSerializer, IPVRMatrixSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('name')
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

class IPVRMatrixViewSet(viewsets.ModelViewSet):
    queryset = IPVRMatrix.objects.all().order_by('task', 'hazard')
    serializer_class = IPVRMatrixSerializer
    permission_classes = [AllowAny]
