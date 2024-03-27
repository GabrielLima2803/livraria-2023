from rest_framework.viewsets import ModelViewSet

from core.models import Livro

from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from core.serializers import LivroSerializer, LivroDetailSerializer, LivroListSerializer

class LivroViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categoria__descricao", "editora__nome"]
    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
