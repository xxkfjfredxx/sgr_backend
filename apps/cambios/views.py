from rest_framework import viewsets
from .models import ChangeRequest, ChangeEvaluation, ChangeImplementation
from .serializers import ChangeRequestSerializer, ChangeEvaluationSerializer, ChangeImplementationSerializer

class ChangeRequestViewSet(viewsets.ModelViewSet):
    queryset = ChangeRequest.objects.all().order_by('-created_at')
    serializer_class = ChangeRequestSerializer

class ChangeEvaluationViewSet(viewsets.ModelViewSet):
    queryset = ChangeEvaluation.objects.all().order_by('-evaluated_at')
    serializer_class = ChangeEvaluationSerializer

class ChangeImplementationViewSet(viewsets.ModelViewSet):
    queryset = ChangeImplementation.objects.all().order_by('-implementation_date')
    serializer_class = ChangeImplementationSerializer
