from rest_framework import viewsets
from .models import LegalRequirement
from .serializers import LegalRequirementSerializer

class LegalRequirementViewSet(viewsets.ModelViewSet):
    queryset = LegalRequirement.objects.all().order_by('-created_at')
    serializer_class = LegalRequirementSerializer
