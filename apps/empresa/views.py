from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django_tenants.utils import schema_context, get_public_schema_name
from apps.utils.auditlogmimix import AuditLogMixin
from .models import Company
from .serializers import CompanySerializer
from django.db.models.deletion import ProtectedError


import logging
logger = logging.getLogger(__name__)

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        incluir_eliminadas = self.request.query_params.get("incluir_eliminadas") == "true"
        
        if not user.is_superuser:
            return Company.objects.none()
        
        qs = Company.objects.all()
        if not incluir_eliminadas:
            qs = qs.filter(is_deleted=False)
        return qs

    #def delete(self, *args, **kwargs):
    #    raise ValidationError("Usa el método eliminar_definitivo para borrar completamente una empresa.")

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_superuser:
            raise serializers.ValidationError({"detail": "Solo el superusuario puede crear empresas."})

        company = serializer.save()

        try:
            with schema_context(company.schema_name):
                call_command('migrate', interactive=False, verbosity=0)
        except Exception as e:
            logger.error(f"Error al migrar el esquema '{company.schema_name}': {str(e)}")
            company.delete()
            raise serializers.ValidationError({"detail": "Error al aplicar migraciones del esquema. Empresa eliminada."})

    @action(detail=False, methods=["get"], url_path="my-companies")
    def my_companies(self, request):
        user = request.user

        if user.is_superuser:
            qs = self.get_queryset()
        else:
            qs = Company.objects.none()

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="me")
    def me(self, request):
        company = getattr(request, "active_company", None)

        if not company:
            if request.user.is_authenticated and hasattr(request.user, "company"):
                company = request.user.company

        if not company:
            return Response(
                {"detail": "No se encontró una empresa activa para este usuario."},
                status=400
            )

        serializer = self.get_serializer(company)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        # ⚠️ No uses self.get_object() aquí porque no incluye eliminadas
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'detail': 'Empresa no encontrada'}, status=404)

        company.is_deleted = False
        company.is_active = True
        company.save()
        return Response({'status': 'Restaurada'})


    @action(detail=True, methods=['delete'], url_path='eliminar-definitivo')
    def eliminar_definitivo(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)  # 👈 Buscar directamente, incluye eliminadas
        except Company.DoesNotExist:
            return Response({'detail': 'Empresa no encontrada'}, status=404)

        if company.schema_name == get_public_schema_name():
            raise ValidationError("No puedes eliminar el esquema público.")
        
        try:
            with schema_context(company.schema_name):
                from apps.usuarios.models import User, UserRole
                from django.apps import apps

                UserRole.objects.all().delete()
                User.objects.all().delete()

                # Limpia otras tablas (opcional)
                connection = apps.get_app_config('your_app_name').connection
                with connection.cursor() as cursor:
                    cursor.execute("""
                        DO $$
                        DECLARE
                            tablename text;
                        BEGIN
                            FOR tablename IN
                                SELECT tablename
                                FROM pg_tables
                                WHERE schemaname = current_schema() AND tablename != 'django_migrations'
                            LOOP
                                EXECUTE format('DELETE FROM %I', tablename);
                            END LOOP;
                        END;
                        $$;
                    """)
        except Exception as e:
            return Response(
                {'detail': f"No se puede eliminar porque el schema está corrupto o incompleto: {str(e)}"},
                status=500
            )

        try:
            company.delete()
            return Response({'status': 'Eliminada completamente'})
        except ProtectedError as e:
            return Response({'detail': f"Error de integridad: {str(e)}"}, status=400)
        except Exception as e:
            return Response({'detail': f"Error al eliminar: {str(e)}"}, status=500)


    def destroy(self, request, *args, **kwargs):
        company = self.get_object()

        if company.schema_name == get_public_schema_name():
            raise ValidationError("No puedes eliminar el esquema público.")

        company.is_deleted = True
        company.is_active = False
        company.save()
        return Response({'status': 'Empresa desactivada (soft delete)'}, status=204)
