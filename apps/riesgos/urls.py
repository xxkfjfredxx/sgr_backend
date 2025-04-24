from rest_framework.routers import DefaultRouter
from .views import AreaViewSet, HazardViewSet, RiskAssessmentViewSet

router = DefaultRouter()
router.register(r'areas', AreaViewSet, basename='area')
router.register(r'hazards', HazardViewSet, basename='hazard')
router.register(r'risk-assessments', RiskAssessmentViewSet, basename='riskassessment')

urlpatterns = router.urls