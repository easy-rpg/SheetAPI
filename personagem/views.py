from rest_framework.viewsets import ModelViewSet
from .models import Personagem, PersonagemClasse
from .serializers import PersonagemSerializer, PersonagemClasseSerializer


class PersonagemViewSet(ModelViewSet):
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
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
