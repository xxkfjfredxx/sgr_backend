from django_tenants.middleware.main import TenantMainMiddleware
from django.core.exceptions import PermissionDenied
from apps.empresa.models import Company  # Asegúrate de importar Company
from django_tenants.utils import tenant_context
from rest_framework.authentication import TokenAuthentication  # ✅
from rest_framework.exceptions import AuthenticationFailed

class TenantMiddleware(TenantMainMiddleware):
    def process_request(self, request):
        print("Verificando el middleware: Proceso de asignación de compañía activa")

        # Excluir login/logout
        if request.path.startswith("/api/login/") or request.path.startswith("/api/logout/"):
            return

        # 👇 Autenticación manual
        try:
            user_auth_tuple = TokenAuthentication().authenticate(request)
            if user_auth_tuple is not None:
                request.user, request.auth = user_auth_tuple
        except AuthenticationFailed:
            raise PermissionDenied("Token inválido o expirado")

        # 👇 Ahora sí ya puedes validar si el usuario está autenticado
        if not request.user.is_authenticated:
            raise PermissionDenied("Usuario no autenticado")

        # Obtener tenant desde header
        company_id = request.headers.get("X-Active-Company")
        if not company_id:
            return

        if not company_id.isdigit():
            raise PermissionDenied("X-Active-Company inválido")

        try:
            company = Company.objects.get(pk=int(company_id))
        except Company.DoesNotExist:
            raise PermissionDenied("Compañía no encontrada")

        request.tenant = company
        request._tenant_context = tenant_context(company)
        request._tenant_context.__enter__()

        request.active_company = company

    def process_response(self, request, response):
        if hasattr(request, "_tenant_context"):
            request._tenant_context.__exit__(None, None, None)
        return response
