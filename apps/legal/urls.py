from rest_framework.routers import DefaultRouter
from .views import LegalRequirementViewSet

router = DefaultRouter()
router.register(r'legal-requirements', LegalRequirementViewSet)

urlpatterns = router.urls
