from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter

from usuario.models import Usuario

from core.models import Compra

from core.serializers import CompraSerializer, CriarEditarCompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["usuario", "status", "data"]
    search_fields = ["usuario__email"]
    ordering_fields = ["usuario", "status", "data"]
    ordering = ["usuario__email"]



    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarCompraSerializer
        return CompraSerializer
    
    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_authenticated: 
            if usuario.tipo == Usuario.TipoUsuario.GERENTE:
                return Compra.objects.all()
            if usuario.is_superuser:
                return Compra.objects.all()
            if usuario.groups.filter(name="Administradores").exists():
                return Compra.objects.all()
            return Compra.objects.filter(usuario=usuario)
        else:
            return Compra.objects.none()