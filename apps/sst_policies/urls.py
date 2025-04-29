from rest_framework.routers import DefaultRouter
from .views import SSTPolicyViewSet, PolicyAcceptanceViewSet

router = DefaultRouter()
router.register(r"sst-policies", SSTPolicyViewSet)
router.register(r"policy-acceptances", PolicyAcceptanceViewSet)

urlpatterns = router.urls
