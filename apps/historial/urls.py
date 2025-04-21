from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkHistoryViewSet

router = DefaultRouter()
router.register(r'work-history', WorkHistoryViewSet, basename='work-history')

urlpatterns = [
    path('', include(router.urls)),
]