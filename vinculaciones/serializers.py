from rest_framework import serializers
from .models import EmploymentLink

class EmploymentLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentLink
        fields = '__all__'