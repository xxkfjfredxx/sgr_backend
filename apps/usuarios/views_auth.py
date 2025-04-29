# apps/usuarios/views_auth.py
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer


class LoginView(APIView):
    """
    POST /login/  – Devuelve token y datos de usuario.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response(
                {"error": "Credenciales inválidas"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # 1️⃣ cerramos sesión anterior (opcional) y creamos nueva
        login(request, user)

        # 2️⃣ eliminamos tokens previos para evitar duplicados
        Token.objects.filter(user=user).delete()

        # 3️⃣ generamos token limpio
        token = Token.objects.create(user=user)

        return Response(
            {
                "token": token.key,
                "user": UserSerializer(user).data,
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
