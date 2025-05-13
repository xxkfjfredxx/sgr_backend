from rest_framework.routers import DefaultRouter
from .views import (
    AreaViewSet,
    HazardViewSet,
    RiskAssessmentViewSet,
    RiskControlViewSet,
    RiskReviewViewSet,
    RiskActionViewSet,
    ControlEvidenceViewSet,
    ControlFollowUpViewSet,
)

router = DefaultRouter()
router.register(r"areas", AreaViewSet, basename="area")
router.register(r"hazards", HazardViewSet, basename="hazard")
router.register(r"risk-assessments", RiskAssessmentViewSet, basename="riskassessment")
router.register(r"risk-controls", RiskControlViewSet, basename="risk-control")
router.register(r"risk-reviews", RiskReviewViewSet, basename="risk-review")
router.register(r"risk-actions", RiskActionViewSet, basename="risk-action")
router.register(r"control-evidences", ControlEvidenceViewSet)
router.register(r"control-followups", ControlFollowUpViewSet)

urlpatterns = router.urls
