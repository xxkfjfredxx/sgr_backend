from rest_framework.routers import DefaultRouter
from .views import ImprovementPlanViewSet, ActionItemViewSet,RiskActionViewSet

router = DefaultRouter()
router.register(r'improvement-plans', ImprovementPlanViewSet, basename='improvementplan')
router.register(r'action-items', ActionItemViewSet, basename='actionitem')
router.register(r'risk-actions', RiskActionViewSet)

urlpatterns = router.urls