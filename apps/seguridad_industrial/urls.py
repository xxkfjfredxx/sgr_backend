from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkAccidentViewSet, WorkAtHeightPermitViewSet

router = DefaultRouter()
router.register(r"work-accidents", WorkAccidentViewSet, basename="work-accidents")
router.register(
    r"work-at-height-permits",
    WorkAtHeightPermitViewSet,
    basename="work-at-height-permits",
)

urlpatterns = [
    path("", include(router.urls)),
]
