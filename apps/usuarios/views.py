from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import EsRolPermitido
from apps.auditoria.utils import AuditLogMixin

class UserRoleViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class UserViewSet(AuditLogMixin,viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer