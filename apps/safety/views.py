from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from .models import SignageInventory, VaccinationRecord
from .serializers import SignageInventorySerializer, VaccinationRecordSerializer


class SignageInventoryViewSet(ModelViewSet):
    queryset = SignageInventory.objects.all()
    serializer_class = SignageInventorySerializer
    parser_classes = [MultiPartParser, FormParser]


class VaccinationRecordViewSet(ModelViewSet):
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordSerializer
    parser_classes = [MultiPartParser, FormParser]
