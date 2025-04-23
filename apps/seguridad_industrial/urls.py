from rest_framework.routers import DefaultRouter
from .views import WorkAccidentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'work-accidents', WorkAccidentViewSet, basename='workaccident')

urlpatterns = [
    path('', include(router.urls)),
] 
