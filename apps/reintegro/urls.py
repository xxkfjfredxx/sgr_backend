from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReintegroViewSet

router = DefaultRouter()
router.register(r"reintegrations", ReintegroViewSet, basename="reintegration")

urlpatterns = [
    path("", include(router.urls)),
]
