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
from apps.salud_ocupacional.views import MedicalExamViewSet
from apps.ausentismo.views import AbsenceViewSet
from apps.capacitaciones.views import (
    TrainingSessionViewSet, TrainingSessionAttendanceViewSet
)
from apps.seguridad_industrial.views import (
    WorkAccidentViewSet,
    WorkAtHeightPermitViewSet,
)
from apps.reintegro.views import ReintegroViewSet
from apps.pausas_activas.views import (
    ActivePauseSessionViewSet, ActivePauseAttendanceViewSet
)
from apps.indicadores.views import IndicatorViewSet, IndicatorResultViewSet
from apps.alertas.views import DocumentAlertViewSet
from apps.acciones_correctivas.views import ImprovementPlanViewSet, ActionItemViewSet
from apps.sst_policies.views import SSTPolicyViewSet, PolicyAcceptanceViewSet
# NUEVAS APPS
# Inspecciones y checklists
from apps.inspecciones.views import (
    InspectionTemplateViewSet,
    InspectionItemViewSet,
    InspectionViewSet,
    InspectionResponseViewSet,
)

from apps.emergencies.views import (
    EmergencyBrigadeMemberViewSet, 
    EmergencyEquipmentViewSet, 
    EmergencyDrillViewSet
)

# EPP
from apps.epp.views import EPPItemViewSet, EPPAssignmentViewSet

# Matriz de riesgos
from apps.riesgos.views import AreaViewSet, HazardViewSet, RiskAssessmentViewSet

# Acceso/egreso y firma de aceptación de riesgos
from apps.accesos.views import AccessLogViewSet, RiskAcceptanceFormViewSet

from apps.stakeholders.views import StakeholderViewSet
from apps.legal.views import LegalRequirementViewSet

from apps.suggestions.views import SuggestionBoxViewSet

# Crear router
router = DefaultRouter()

# Endpoints estándar
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
router.register(r'medical-exams', MedicalExamViewSet)
router.register(r'absences', AbsenceViewSet)
router.register(r'training-sessions', TrainingSessionViewSet)
router.register(r'training-attendance', TrainingSessionAttendanceViewSet)
router.register(r'work-accidents', WorkAccidentViewSet)
router.register(r'improvement-plans', ImprovementPlanViewSet)
router.register(r'action-items', ActionItemViewSet)
router.register(r'work-at-height-permits', WorkAtHeightPermitViewSet)
router.register(r'reintegrations', ReintegroViewSet)
router.register(r'pausas-sessions', ActivePauseSessionViewSet)
router.register(r'pausas-attendance', ActivePauseAttendanceViewSet)
router.register(r'indicators', IndicatorViewSet)
router.register(r'indicator-results', IndicatorResultViewSet)
router.register(r'document-alerts', DocumentAlertViewSet)
router.register(r'stakeholders', StakeholderViewSet)
router.register(r'legal-requirements', LegalRequirementViewSet)
router.register(r'sst-policies', SSTPolicyViewSet)
router.register(r'policy-acceptances', PolicyAcceptanceViewSet)
router.register(r'suggestions', SuggestionBoxViewSet)
router.register(r'emergency-brigade', EmergencyBrigadeMemberViewSet)
router.register(r'emergency-equipment', EmergencyEquipmentViewSet)
router.register(r'emergency-drills', EmergencyDrillViewSet)

# Inspecciones
router.register(r'inspection-templates', InspectionTemplateViewSet)
router.register(r'inspection-items', InspectionItemViewSet)
router.register(r'inspections', InspectionViewSet)
router.register(r'inspection-responses', InspectionResponseViewSet)

# EPP
router.register(r'epp-items', EPPItemViewSet)
router.register(r'epp-assignments', EPPAssignmentViewSet)

# Matriz de riesgos
router.register(r'areas', AreaViewSet)
router.register(r'hazards', HazardViewSet)
router.register(r'risk-assessments', RiskAssessmentViewSet)

# Accesos y firmas de aceptación
router.register(r'access-logs', AccessLogViewSet)
router.register(r'risk-acceptances', RiskAcceptanceFormViewSet)

urlpatterns = router.urls
