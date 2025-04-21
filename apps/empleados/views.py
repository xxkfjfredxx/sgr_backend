from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.empleados.models import Employee
from rest_framework.permissions import AllowAny
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]
    