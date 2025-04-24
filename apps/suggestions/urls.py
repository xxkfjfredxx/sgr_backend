from rest_framework.routers import DefaultRouter
from .views import SuggestionBoxViewSet

router = DefaultRouter()
router.register(r'suggestions', SuggestionBoxViewSet)

urlpatterns = router.urls
