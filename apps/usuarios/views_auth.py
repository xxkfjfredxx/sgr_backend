# apps/usuarios/views_auth.py
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from django_tenants.utils import tenant_context
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response(
                {"detail": "Credenciales inválidas"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        tenant_id = None
        company_name = None

        # Distinción clara: superuser vs usuario normal
        if user.is_superuser:
            user_data = {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "is_superuser": True,
            }
        else:
            try:
                from apps.empleados.models import Employee
                employee = Employee.objects.get(user=user)
                company = employee.company
                tenant_id = str(company.id)
                company_name = company.name
            except Exception:
                return Response(
                    {"detail": "El usuario no tiene un empleado o empresa asociada"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Si no es superuser, sí usamos el serializer completo
            user_data = UserSerializer(user).data

        # Elimina tokens viejos y crea uno nuevo
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        login(request, user)

        return Response(
            {
                "token": token.key,
                "user": user_data,
                "tenant_id": tenant_id,
                "company_name": company_name,
            },
            status=status.HTTP_200_OK,
        )


class LogoutView(APIView):
    """
    POST /logout/  – Borra token y cierra sesión. Idempotente.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # 1️⃣ Elimina el token si existe
        Token.objects.filter(user=request.user).delete()

        # 2️⃣ Cierra la sesión de Django
        logout(request)

        # 3️⃣ Siempre responde 200 OK (idempotencia)
        return Response(
            {"message": "Sesión cerrada correctamente"},
            status=status.HTTP_200_OK,
        )


class MeView(APIView):
    """
    GET /me/  – Devuelve los datos del usuario autenticado.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)
