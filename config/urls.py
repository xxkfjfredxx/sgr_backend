from django.contrib import admin
from django.urls import path, include
from config.views_api import router  # 👈 el router central

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('usuarios.urls')),
    path('api/', include('documentos.urls')),
    path('api/', include('empleados.urls')),
    path('api/', include('vinculaciones.urls')),
    path('api/', include('historial.urls')),
    path('api/', include('auditoria.urls')),
    path('api/', include('catalogos.urls')),
    path('api/', include('empresa.urls')),
]