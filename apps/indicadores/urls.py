from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    IndicatorViewSet,
    IndicatorResultViewSet,
    indicator_summary  # 👈 importamos el resumen
)

router = DefaultRouter()
router.register(r'indicators', IndicatorViewSet, basename='indicator')
router.register(r'indicator-results', IndicatorResultViewSet, basename='indicatorresult')

# Agrega aquí tu endpoint adicional
urlpatterns = router.urls + [
    path('summary/', indicator_summary, name='indicator-summary'),
]