from rest_framework.routers import DefaultRouter
from .views import DocumentAlertViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"document-alerts", DocumentAlertViewSet, basename="documentalert")

urlpatterns = [
    path("", include(router.urls)),
]
