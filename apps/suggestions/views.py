from rest_framework import viewsets
from .models import SuggestionBox
from .serializers import SuggestionBoxSerializer

class SuggestionBoxViewSet(viewsets.ModelViewSet):
    queryset = SuggestionBox.objects.all().order_by('-created_at')
    serializer_class = SuggestionBoxSerializer
