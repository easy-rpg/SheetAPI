from rest_framework.viewsets import ModelViewSet
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
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
