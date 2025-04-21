from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, PositionViewSet, WorkAreaViewSet, DocumentTypeViewSet

router = DefaultRouter()
router.register(r'branches', BranchViewSet, basename='branches')
router.register(r'positions', PositionViewSet, basename='positions')
router.register(r'work-areas', WorkAreaViewSet, basename='work-areas')
router.register(r'document-types', DocumentTypeViewSet, basename='document-types')

urlpatterns = [
    path('', include(router.urls)),
]