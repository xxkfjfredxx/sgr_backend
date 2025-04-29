from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, PositionViewSet, WorkAreaViewSet

router = DefaultRouter()
router.register(r"branches", BranchViewSet, basename="branches")
router.register(r"positions", PositionViewSet, basename="positions")
router.register(r"work-areas", WorkAreaViewSet, basename="work-areas")

urlpatterns = [
    path("", include(router.urls)),
]
