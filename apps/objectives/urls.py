from rest_framework.routers import DefaultRouter
from .views import SSTObjectiveViewSet, SSTGoalViewSet

router = DefaultRouter()
router.register(r"objectives", SSTObjectiveViewSet, basename="objectives")
router.register(r"goals", SSTGoalViewSet, basename="goals")

urlpatterns = router.urls
