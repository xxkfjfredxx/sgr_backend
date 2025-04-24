from rest_framework.routers import DefaultRouter
from .views import AccessLogViewSet, RiskAcceptanceFormViewSet

router = DefaultRouter()
router.register(r'access-logs', AccessLogViewSet, basename='accesslog')
router.register(r'risk-acceptances', RiskAcceptanceFormViewSet, basename='riskacceptanceform')

urlpatterns = router.urls