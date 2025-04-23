from rest_framework.routers import DefaultRouter
from .views import TrainingSessionViewSet, TrainingSessionAttendanceViewSet

router = DefaultRouter()
router.register(r'training-sessions', TrainingSessionViewSet, basename='trainingsession')
router.register(r'training-attendance', TrainingSessionAttendanceViewSet, basename='trainingattendance')

urlpatterns = router.urls
