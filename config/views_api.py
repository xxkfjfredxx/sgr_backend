from rest_framework.routers import DefaultRouter

# ViewSets existentes
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

# Nuevos ViewSets SG-SST
from apps.salud_ocupacional.views import MedicalExamViewSet
from apps.ausentismo.views import AbsenceViewSet
from apps.capacitaciones.views import (
    TrainingSessionViewSet, TrainingSessionAttendanceViewSet
)
from apps.seguridad_industrial.views import WorkAccidentViewSet
from apps.indicadores.views import IndicatorViewSet, IndicatorResultViewSet
from apps.alertas.views import DocumentAlertViewSet

# Crear router
router = DefaultRouter()

# Registrar endpoints estándar
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'employment-links', EmploymentLinkViewSet)
router.register(r'work-history', WorkHistoryViewSet)
router.register(r'audit', SystemAuditViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'work-areas', WorkAreaViewSet)
router.register(r'document-types', DocumentTypeViewSet)
router.register(r'users', UserViewSet)
router.register(r'user-roles', UserRoleViewSet)
router.register(r'documents', EmployeeDocumentViewSet)

# Registrar endpoints SG-SST
router.register(r'medical-exams', MedicalExamViewSet)
router.register(r'absences', AbsenceViewSet)
router.register(r'training-sessions', TrainingSessionViewSet)
router.register(r'training-attendance', TrainingSessionAttendanceViewSet)
router.register(r'work-accidents', WorkAccidentViewSet)
router.register(r'indicators', IndicatorViewSet)
router.register(r'indicator-results', IndicatorResultViewSet)
router.register(r'document-alerts', DocumentAlertViewSet)

urlpatterns = router.urls
