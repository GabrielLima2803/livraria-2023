from rest_framework.viewsets import ModelViewSet

from core.models import Editora

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter

from core.serializers import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["nome"]
    search_fields = ["nome"]



