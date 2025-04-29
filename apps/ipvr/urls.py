from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, IPVRMatrixViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"ipvr-matrix", IPVRMatrixViewSet, basename="ipvr-matrix")

urlpatterns = [
    path("", include(router.urls)),
]
