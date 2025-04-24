from rest_framework.routers import DefaultRouter
from .views import StakeholderViewSet

router = DefaultRouter()
router.register(r'stakeholders', StakeholderViewSet)

urlpatterns = router.urls