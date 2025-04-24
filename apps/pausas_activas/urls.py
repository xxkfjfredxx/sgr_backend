from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivePauseSessionViewSet, ActivePauseAttendanceViewSet

router = DefaultRouter()
router.register(r'pausas-sessions', ActivePauseSessionViewSet, basename='pausas-sessions')
router.register(r'pausas-attendance', ActivePauseAttendanceViewSet, basename='pausas-attendance')

urlpatterns = [
    path('', include(router.urls)),
]
