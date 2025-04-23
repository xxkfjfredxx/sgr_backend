from rest_framework.routers import DefaultRouter
from .views import DocumentAlertViewSet

router = DefaultRouter()
router.register(r'document-alerts', DocumentAlertViewSet, basename='documentalert')

urlpatterns = router.urls
