from rest_framework.routers import DefaultRouter
from .views import WorkAccidentViewSet

router = DefaultRouter()
router.register(r'work-accidents', WorkAccidentViewSet, basename='workaccident')

urlpatterns = router.urls
