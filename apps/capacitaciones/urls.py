from rest_framework.routers import DefaultRouter
from .views import (
    TrainingSessionViewSet,
    TrainingSessionAttendanceViewSet,
    CertificationViewSet,
)
from django.urls import path, include

router = DefaultRouter()
router.register(
    r"training-sessions", TrainingSessionViewSet, basename="trainingsession"
)
router.register(
    r"training-attendance",
    TrainingSessionAttendanceViewSet,
    basename="trainingattendance",
)
router.register(r"certifications", CertificationViewSet, basename="certification")

urlpatterns = [
    path("", include(router.urls)),
]
