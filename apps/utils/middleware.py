from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied
from apps.empresa.models import Company
from django_multitenant.utils import set_current_tenant

class ActiveCompanyMiddleware(MiddlewareMixin):
    """
    1) Lee X-Active-Company
    2) Valida que el usuario tenga acceso a esa Company
    3) Llama a set_current_tenant() para que el ORM filtre por company_id
    """
    def process_request(self, request):
        header = request.headers.get("X-Active-Company")
        if not header:
            # Si no hay header, dejamos que falle más adelante si es necesario
            return

        if not request.user.is_authenticated or not header.isdigit():
            raise PermissionDenied("X-Active-Company inválido o usuario no autenticado")

        try:
            company = Company.objects.get(pk=int(header))
        except Company.DoesNotExist:
            raise PermissionDenied("Compañía no encontrada")

        # Verifica que el usuario esté asignado a esa compañía
        if not request.user.empresas_asignadas.filter(pk=company.pk).exists():
            raise PermissionDenied("No tienes acceso a esta compañía")

        # Activa el tenant para django-multitenant
        set_current_tenant(company)

        # Guardamos la Company en el request por si la necesitas
        request.active_company = company
