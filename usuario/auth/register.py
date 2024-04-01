from django.db.models import Q
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


from usuario.models import Usuario
from usuario.serializers import UsuarioSerializer

User = get_user_model()

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def AuthRegister(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    if Usuario.objects.filter(username=username).exists():
        return Response(
            {"message": "Usuário já existente!"}, status=status.HTTP_400_BAD_REQUEST
        )
    elif Usuario.objects.filter(email=email).exists():
        return Response(
            {"message": "Email já está sendo utilizado!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if username and email and password:
        user = User.objects.create(username=username)
        user.email = email
        user.set_password(password)
        user.save()

        response_data = {
            "message": "Usuário criado com sucesso!",
            "username": user.username,
            "email": user.email,
            "id": user.id,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Dados de usuário inválidos!"}, status=400)
