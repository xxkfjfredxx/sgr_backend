from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views_auth import LoginView, LogoutView, MeView

router = DefaultRouter()
router.register(r'user-roles', UserRoleViewSet)
router.register(r'users', UserViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'work-areas', WorkAreaViewSet)
router.register(r'document-types', DocumentTypeViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'employment-links', EmploymentLinkViewSet)
router.register(r'personal-documents', PersonalDocumentViewSet)
router.register(r'work-history', WorkHistoryViewSet)
router.register(r'system-audit', SystemAuditViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='me'),
]