from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PersonalDocument
from .serializers import PersonalDocumentSerializer

class PersonalDocumentViewSet(viewsets.ModelViewSet):
    queryset = PersonalDocument.objects.all().order_by('-id')
    serializer_class = PersonalDocumentSerializer
    permission_classes = [IsAuthenticated]
