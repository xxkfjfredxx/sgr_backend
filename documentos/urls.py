from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalDocumentViewSet

router = DefaultRouter()
router.register(r'personal-documents', PersonalDocumentViewSet, basename='personal-documents')

urlpatterns = [
    path('', include(router.urls)),
]