from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    retrieve:
        Retorna um usuário
    list:
        Retorna todos os usuários
    create:
        Cria um novo usuário
    delete:
        Remove um usuário existente
    partial_update:
        Atualiza um ou mais campos de um usuário existente
    update:
        Atualiza um usuário
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    http_method_names = ['get', 'post', 'put', 'patch']

    @action(methods=['get'], detail=False)
    def token(self, request):
        """
        Retorna o usuario pelo token
        """
        return Response(self.serializer_class(request.user).data)
