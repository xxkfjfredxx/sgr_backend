from rest_framework import viewsets
from .models import SSTObjective, SSTGoal
from .serializers import SSTObjectiveSerializer, SSTGoalSerializer

class SSTObjectiveViewSet(viewsets.ModelViewSet):
    queryset = SSTObjective.objects.all().order_by('-created_at')
    serializer_class = SSTObjectiveSerializer

class SSTGoalViewSet(viewsets.ModelViewSet):
    queryset = SSTGoal.objects.all().order_by('-id')
    serializer_class = SSTGoalSerializer
