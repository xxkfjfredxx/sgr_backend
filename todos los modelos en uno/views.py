from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissions import EsRolPermitido

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class WorkAreaViewSet(viewsets.ModelViewSet):
    queryset = WorkArea.objects.all()
    serializer_class = WorkAreaSerializer

class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [EsRolPermitido]
    roles_permitidos = ['SuperAdmin', 'HR']

class EmploymentLinkViewSet(viewsets.ModelViewSet):
    queryset = EmploymentLink.objects.all()
    serializer_class = EmploymentLinkSerializer

class PersonalDocumentViewSet(viewsets.ModelViewSet):
    queryset = PersonalDocument.objects.all()
    serializer_class = PersonalDocumentSerializer

class WorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer

class SystemAuditViewSet(viewsets.ModelViewSet):
    queryset = SystemAudit.objects.all()
    serializer_class = SystemAuditSerializer
