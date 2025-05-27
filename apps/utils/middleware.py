from django.core.exceptions import PermissionDenied
from apps.empresa.models import Company
from django_multitenant.utils import set_current_tenant


class ActiveCompanyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        company_id = request.headers.get("X-Active-Company")
        if request.user.is_authenticated and company_id and company_id.isdigit():
            try:
                company = Company.objects.get(id=company_id)

                # 🔐 Validación de seguridad
                if not request.user.empresas_asignadas.filter(id=company.id).exists():
                    raise PermissionDenied("You don't have access to this company.")

                request.user._active_company = company

            except Company.DoesNotExist:
                request.user._active_company = None

        return self.get_response(request)


class CustomTenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant = getattr(request.user, "active_company", None)
        if tenant:
            set_current_tenant(tenant)
        return self.get_response(request)
