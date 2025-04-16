from django.contrib import admin
from django.urls import path, include
from config.views_api import router  # 👈 el router central

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # 👈 unifica todos los endpoints
]
