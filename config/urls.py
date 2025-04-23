from django.contrib import admin
from django.urls import path, include
from django.conf import settings                     # 👈 Importación para archivos media
from django.conf.urls.static import static           # 👈 Importación para archivos media
from config.views_api import router                  # 👈 el router central

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),   # ELIMINADA ESTA LÍNEA
    path('api/', include('apps.usuarios.urls')),
    path('api/', include('apps.empleados.urls')),
    path('api/', include('apps.vinculaciones.urls')),
    path('api/', include('apps.historial.urls')),
    path('api/', include('apps.auditoria.urls')),
    path('api/', include('apps.catalogos.urls')),
    path('api/', include('apps.empresa.urls')),
    path('api/occupational-health/', include('apps.salud_ocupacional.urls')),
    path('api/absences/', include('apps.ausentismo.urls')),
    path('api/trainings/', include('apps.capacitaciones.urls')),
    path('api/industrial-safety/', include('apps.seguridad_industrial.urls')),
    path('api/indicators/', include('apps.indicadores.urls')),
    path('api/alerts/', include('apps.alertas.urls')),
]

# 👇 Esto sirve los archivos subidos (PDF, Word, Excel, imágenes)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
