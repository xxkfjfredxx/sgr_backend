from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ErgonomicAssessmentViewSet, AROViewSet, ATSViewSet

router = DefaultRouter()
router.register(
    r"ergonomic-assessments",
    ErgonomicAssessmentViewSet,
    basename="ergonomic-assessments",
)
router.register(r"aro", AROViewSet, basename="aro")
router.register(r"ats", ATSViewSet, basename="ats")

urlpatterns = [
    path("", include(router.urls)),
]
