from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DocumentTypeViewSet, EmployeeDocumentViewSet

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employees")
router.register(r"document-types", DocumentTypeViewSet, basename="document-types")
router.register(r"documents", EmployeeDocumentViewSet, basename="documents")


urlpatterns = [
    path("", include(router.urls)),
]
