from django.contrib import admin
from .models import Activity
from apps.utils.admin_mixins import BaseAuditAdmin


@admin.register(Activity)
class ActivityAdmin(BaseAuditAdmin):
    list_display = ["title", "start_date", "status", "company", "created_by"]
    list_filter = ["status", "company"]
    search_fields = ["title", "description"]
