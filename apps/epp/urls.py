from rest_framework.routers import DefaultRouter
from .views import EPPItemViewSet, EPPAssignmentViewSet

router = DefaultRouter()
router.register(r"epp-items", EPPItemViewSet, basename="eppitem")
router.register(r"epp-assignments", EPPAssignmentViewSet, basename="eppassignment")

urlpatterns = router.urls
