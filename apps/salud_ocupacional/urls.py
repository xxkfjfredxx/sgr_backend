from rest_framework.routers import DefaultRouter
from .views import MedicalExamViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"medical-exams", MedicalExamViewSet, basename="medicalexam")

urlpatterns = [
    path("", include(router.urls)),
]
