from rest_framework.routers import DefaultRouter
from .views import AbsenceViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"absences", AbsenceViewSet, basename="absence")

urlpatterns = [
    path("", include(router.urls)),
]
