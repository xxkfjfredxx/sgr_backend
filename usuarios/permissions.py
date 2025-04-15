from rest_framework import permissions

class EsRolPermitido(permissions.BasePermission):
    """
    Permite el acceso solo si el usuario tiene un rol específico.
    """

    def has_permission(self, request, view):
        usuario = request.user
        if not usuario.is_authenticated:
            return False

        # Aquí defines los roles permitidos por vista
        roles_permitidos = getattr(view, 'roles_permitidos', None)

        if roles_permitidos is None:
            return True  # Si no se especifican, permite acceso

        return usuario.rol.nombre in roles_permitidos
