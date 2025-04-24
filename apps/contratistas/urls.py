from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContractorCompanyViewSet, ContractorContactViewSet

router = DefaultRouter()
router.register(r'contractors', ContractorCompanyViewSet, basename='contractors')
router.register(r'contractor-contacts', ContractorContactViewSet, basename='contractor-contacts')

urlpatterns = [
    path('', include(router.urls)),
]
