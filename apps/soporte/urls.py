from rest_framework.routers import DefaultRouter
from .views import (
    SupportTicketViewSet,
    MaintenanceScheduleViewSet,
    MaintenanceRecordViewSet,
)

router = DefaultRouter()
router.register(r"support-tickets", SupportTicketViewSet, basename="support-ticket")
router.register(
    r"maintenance-schedules",
    MaintenanceScheduleViewSet,
    basename="maintenance-schedule",
)
router.register(
    r"maintenance-records", MaintenanceRecordViewSet, basename="maintenance-record"
)

urlpatterns = router.urls
