from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from core.models import Compra

from core.serializers import CompraSerializer, CriarEditarCompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["usuario_username"]


    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarCompraSerializer
        return CompraSerializer
    
    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_authenticated: 
            if usuario.is_superuser:
                return Compra.objects.all()
            if usuario.groups.filter(name="Administradores").exists():
                return Compra.objects.all()
            return Compra.objects.filter(usuario=usuario)
        else:
            return Compra.objects.none()