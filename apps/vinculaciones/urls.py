from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmploymentLinkViewSet

router = DefaultRouter()
router.register(r"employment-links", EmploymentLinkViewSet, basename="employment-links")

urlpatterns = [
    path("", include(router.urls)),
]
