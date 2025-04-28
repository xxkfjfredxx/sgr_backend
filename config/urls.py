from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.views_api import router  # Tu router central

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),   # 👈 SOLO ESTA línea para todos los endpoints
    path('api/', include('apps.usuarios.urls')),  # 👈 LOGIN, LOGOUT, ME manualmente
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
