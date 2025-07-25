from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.auditlogmimix import AuditLogMixin

from .models import Branch, Position, WorkArea
from .serializers import BranchSerializer, PositionSerializer, WorkAreaSerializer


class BaseCatalogViewSet(AuditLogMixin, viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    # — filtro por ?name=<texto> —
    def get_queryset(self):
        qs = super().get_queryset()
        if name := self.request.query_params.get("name"):
            qs = qs.filter(name__icontains=name)
        return qs

    # — restaurar borrado lógico —
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Registro restaurado."}, status=status.HTTP_200_OK)


class BranchViewSet(BaseCatalogViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def get_queryset(self):
        company = self.request.user.company
        return Branch.objects.filter(company=company)
    
    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


class PositionViewSet(BaseCatalogViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def get_queryset(self):
        company = self.request.user.company
        return Position.objects.filter(company=company)
    
    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)

class WorkAreaViewSet(BaseCatalogViewSet):
    queryset = WorkArea.objects.all()
    serializer_class = WorkAreaSerializer

    def get_queryset(self):
        company = self.request.user.company
        return WorkArea.objects.filter(company=company)
    
    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)
