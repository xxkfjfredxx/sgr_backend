from rest_framework.routers import DefaultRouter
from .views import SignageInventoryViewSet, VaccinationRecordViewSet

router = DefaultRouter()
router.register(r"signage", SignageInventoryViewSet, basename="signage")
router.register(r"vaccinations", VaccinationRecordViewSet, basename="vaccinations")

urlpatterns = router.urls
