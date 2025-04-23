from rest_framework.routers import DefaultRouter
from .views import MedicalExamViewSet

router = DefaultRouter()
router.register(r'medical-exams', MedicalExamViewSet, basename='medicalexam')

urlpatterns = router.urls
