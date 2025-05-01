from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, MyCompaniesView

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="companies")

urlpatterns = [
    path("", include(router.urls)),
    path("my-companies/", MyCompaniesView.as_view(), name="my-companies"),
]
