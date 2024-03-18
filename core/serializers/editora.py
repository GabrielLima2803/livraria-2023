from rest_framework.serializers import ModelSerializer

from core.models import Editora

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = ["id", "nome", "site"]