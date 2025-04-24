from rest_framework.routers import DefaultRouter
from .views import EmergencyBrigadeMemberViewSet, EmergencyEquipmentViewSet, EmergencyDrillViewSet

router = DefaultRouter()
router.register(r'emergency-brigade', EmergencyBrigadeMemberViewSet)
router.register(r'emergency-equipment', EmergencyEquipmentViewSet)
router.register(r'emergency-drills', EmergencyDrillViewSet)

urlpatterns = router.urls
