from rest_framework import serializers
from .models import PersonalDocument

class PersonalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDocument
        fields = '__all__'