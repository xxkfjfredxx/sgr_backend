from rest_framework import serializers
from .models import SuggestionBox

class SuggestionBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionBox
        fields = '__all__'
