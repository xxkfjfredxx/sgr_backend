from rest_framework import viewsets
from .models import Stakeholder
from .serializers import StakeholderSerializer

class StakeholderViewSet(viewsets.ModelViewSet):
    queryset = Stakeholder.objects.all().order_by('name')
    serializer_class = StakeholderSerializer