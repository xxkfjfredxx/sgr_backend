from rest_framework.routers import DefaultRouter
from .views import AbsenceViewSet

router = DefaultRouter()
router.register(r'absences', AbsenceViewSet, basename='absence')

urlpatterns = router.urls