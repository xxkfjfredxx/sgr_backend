from rest_framework import viewsets
from .models import ImprovementPlan, ActionItem
from .serializers import ImprovementPlanSerializer, ActionItemSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny

class ImprovementPlanViewSet(viewsets.ModelViewSet):
    queryset = ImprovementPlan.objects.all().order_by('-created_at')
    serializer_class = ImprovementPlanSerializer
    permission_classes = [AllowAny]

class ActionItemViewSet(viewsets.ModelViewSet):
    queryset = ActionItem.objects.all().order_by('-due_date')
    serializer_class = ActionItemSerializer
    permission_classes = [AllowAny]
