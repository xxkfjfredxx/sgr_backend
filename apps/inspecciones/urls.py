from rest_framework.routers import DefaultRouter
from .views import (
    InspectionTemplateViewSet, InspectionItemViewSet,
    InspectionViewSet, InspectionResponseViewSet
)

router = DefaultRouter()
router.register(r'inspection-templates', InspectionTemplateViewSet, basename='inspectiontemplate')
router.register(r'inspection-items', InspectionItemViewSet, basename='inspectionitem')
router.register(r'inspections', InspectionViewSet, basename='inspection')
router.register(r'inspection-responses', InspectionResponseViewSet, basename='inspectionresponse')

urlpatterns = router.urls