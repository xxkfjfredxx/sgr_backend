from rest_framework.routers import DefaultRouter

# Importa todos los ViewSets
from apps.empresa.views import CompanyViewSet
from apps.empleados.views import (
    EmployeeViewSet,
    EmployeeDocumentViewSet,
    DocumentTypeViewSet,
)
from apps.vinculaciones.views import EmploymentLinkViewSet
from apps.historial.views import WorkHistoryViewSet
from apps.auditoria.views import SystemAuditViewSet
from apps.catalogos.views import (
    BranchViewSet, PositionViewSet, WorkAreaViewSet
)
from apps.usuarios.views import UserViewSet, UserRoleViewSet

# Crear router
router = DefaultRouter()

# Registrar endpoints
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'employment-links', EmploymentLinkViewSet)
router.register(r'work-history', WorkHistoryViewSet)
router.register(r'audit', SystemAuditViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'work-areas', WorkAreaViewSet)
router.register(r'document-types', DocumentTypeViewSet)  # ✅ solo una vez aquí
router.register(r'users', UserViewSet)
router.register(r'user-roles', UserRoleViewSet)
router.register(r'documents', EmployeeDocumentViewSet)
