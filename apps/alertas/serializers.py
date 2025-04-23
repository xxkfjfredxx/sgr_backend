from rest_framework import serializers
from .models import DocumentAlert

class DocumentAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentAlert
        fields = '__all__'
