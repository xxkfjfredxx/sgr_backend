from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import EmploymentLink
from .serializers import EmploymentLinkSerializer

class EmploymentLinkViewSet(viewsets.ModelViewSet):
    queryset = EmploymentLink.objects.all().order_by('-id')
    serializer_class = EmploymentLinkSerializer
    permission_classes = [IsAuthenticated]

