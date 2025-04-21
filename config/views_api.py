from rest_framework.routers import DefaultRouter

# Importa todos los ViewSets
from apps.empresa.views import CompanyViewSet
from apps.empleados.views import EmployeeViewSet
from apps.vinculaciones.views import EmploymentLinkViewSet
from apps.documentos.views import PersonalDocumentViewSet
from apps.historial.views import WorkHistoryViewSet
from apps.auditoria.views import SystemAuditViewSet
from apps.catalogos.views import (
    BranchViewSet, PositionViewSet, WorkAreaViewSet, DocumentTypeViewSet
)
from apps.usuarios.views import UserViewSet, UserRoleViewSet

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
