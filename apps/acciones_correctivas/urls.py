from rest_framework.routers import DefaultRouter
from .views import ImprovementPlanViewSet, ActionItemViewSet

router = DefaultRouter()
router.register(r'improvement-plans', ImprovementPlanViewSet, basename='improvementplan')
router.register(r'action-items', ActionItemViewSet, basename='actionitem')

urlpatterns = router.urls