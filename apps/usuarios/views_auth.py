# apps/usuarios/views_auth.py
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer


class LoginView(APIView):
    permission_classes      = [permissions.AllowAny]
    authentication_classes  = []          # 👈  ignora token entrante

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response(
                {"detail": "Credenciales inválidas"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # reglas multitenant …
        if not user.is_superuser:
            if user.company is None:
                return Response({"detail": "Usuario sin empresa"}, status=400)
            if user.role is None:
                return Response({"detail": "Usuario sin rol"}, status=400)

        # genera token limpio
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        login(request, user)

        return Response(
            {"token": token.key, "user": UserSerializer(user).data},
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
