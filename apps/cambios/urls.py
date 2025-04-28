from rest_framework.routers import DefaultRouter
from .views import ChangeRequestViewSet, ChangeEvaluationViewSet, ChangeImplementationViewSet

router = DefaultRouter()
router.register(r'change-requests', ChangeRequestViewSet, basename='change-request')
router.register(r'change-evaluations', ChangeEvaluationViewSet, basename='change-evaluation')
router.register(r'change-implementations', ChangeImplementationViewSet, basename='change-implementation')


urlpatterns = router.urls
