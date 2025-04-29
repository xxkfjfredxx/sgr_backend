from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from apps.utils.auditlogmimix import AuditLogMixin

from .models import SuggestionBox
from .serializers import SuggestionBoxSerializer


class SuggestionBoxViewSet(AuditLogMixin, viewsets.ModelViewSet):
    queryset = SuggestionBox.objects.filter(is_deleted=False)
    serializer_class = SuggestionBoxSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if typ := self.request.query_params.get("type"):
            qs = qs.filter(type=typ)
        if resp := self.request.query_params.get("responded"):
            qs = qs.filter(responded=resp.lower() == "true")
        if d := self.request.query_params.get("from"):
            if dt := parse_date(d):
                qs = qs.filter(created_at__date__gte=dt)
        return qs

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = self.get_object()
        obj.restore()
        self.log_audit("RESTORED", obj)
        return Response({"detail": "Sugerencia restaurada."}, status=status.HTTP_200_OK)
