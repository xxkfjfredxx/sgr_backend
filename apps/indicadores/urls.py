from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    IndicatorViewSet,
    IndicatorResultViewSet,
    indicator_summary
)

router = DefaultRouter()
router.register(r'', IndicatorViewSet, basename='indicator')
router.register(r'results', IndicatorResultViewSet, basename='indicatorresult')

urlpatterns = [
    path('summary/', indicator_summary, name='indicator-summary'),  # <--- ¡Esto primero!
] + router.urls
