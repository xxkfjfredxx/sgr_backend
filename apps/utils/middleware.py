from django_tenants.middleware.main import TenantMainMiddleware
from django.core.exceptions import PermissionDenied
from apps.empresa.models import Company  # Asegúrate de importar Company
from django_tenants.utils import tenant_context

import tenant

class TenantMiddleware(TenantMainMiddleware):
    """
    1) Lee el header X-Active-Company.
    2) Valida que el usuario esté autenticado y tenga acceso a esa compañía.
    3) Llama a set_current_tenant() para que el ORM filtre por company_id.
    """
    def process_request(self, request):
        print("Verificando el middleware: Proceso de asignación de compañía activa")
        # Excluir login/logout
        if request.path.startswith("/api/login/") or request.path.startswith("/api/logout/"):
            return  # Excluir login/logout
        # Obtener el tenant (empresa) desde el header 'X-Active-Company'
        company_id = request.headers.get("X-Active-Company")
        
        # Si no se proporciona el header, no se hace nada, y se permitirá continuar más tarde.
        if not company_id:
            return
        
        # Verificar si el header contiene un valor válido
        if not company_id.isdigit():
            raise PermissionDenied("X-Active-Company inválido")

        # Convertir el valor de company_id en entero y obtener la compañía correspondiente
        try:
            company = Company.objects.get(pk=int(company_id))
        except Company.DoesNotExist:
            raise PermissionDenied("Compañía no encontrada")

        # Verificar si el usuario está autenticado y tiene acceso a esa compañía
        if not request.user.is_authenticated:
            raise PermissionDenied("Usuario no autenticado")
        
        # Verificar que el usuario tenga acceso a la compañía
        if not request.user.empresas_asignadas.filter(pk=company.pk).exists():
            raise PermissionDenied("No tienes acceso a esta compañía")

        # Establecer el tenant actual para que django_tenants filtre las consultas por la compañía
        request.tenant = tenant  # para compatibilidad
        request._tenant_context = tenant_context(tenant)
        request._tenant_context.__enter__()

        # Guardamos la Company en el request por si se necesita más adelante
        request.active_company = company

    def process_response(self, request, response):
        if hasattr(request, "_tenant_context"):
            request._tenant_context.__exit__(None, None, None)
        return response

