from rest_framework.routers import DefaultRouter

# Importa todos los ViewSets
from empresa.views import CompanyViewSet
from empleados.views import EmployeeViewSet
from vinculaciones.views import EmploymentLinkViewSet
from documentos.views import PersonalDocumentViewSet
from historial.views import WorkHistoryViewSet
from auditoria.views import SystemAuditViewSet
from catalogos.views import (
    BranchViewSet, PositionViewSet, WorkAreaViewSet, DocumentTypeViewSet
)
from usuarios.views import UserViewSet, UserRoleViewSet

router = DefaultRouter()

# Registra todos los endpoints
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'employment-links', EmploymentLinkViewSet)
router.register(r'documents', PersonalDocumentViewSet)
router.register(r'work-history', WorkHistoryViewSet)
router.register(r'audit', SystemAuditViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'work-areas', WorkAreaViewSet)
router.register(r'document-types', DocumentTypeViewSet)
router.register(r'users', UserViewSet)
router.register(r'user-roles', UserRoleViewSet)
