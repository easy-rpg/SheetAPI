from rest_framework.viewsets import ModelViewSet
from .models import Personagem, PersonagemClasse, PersonagemModelo, PersonagemAtributo
from .serializers import PersonagemSerializer, PersonagemClasseSerializer, PersonagemModeloSerializer, \
    PersonagemAtributoSerializer


class PersonagemViewSet(ModelViewSet):
    """
    retrieve:
        Retorna um personagem
    list:
        Retorna todos os personagens
    create:
        Cria um novo personagem
    delete:
        Remove um personagem existente
    partial_update:
        Atualiza um ou mais campos de um personagem existente
    update:
        Atualiza um personagem
    """
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class PersonagemClasseViewSet(ModelViewSet):
    """
    create:
        Adiciona uma nova classe a um personagem existente
    partial_update:
        Atualiza um ou mais campos de uma classe de um personagem existente
    """
    queryset = PersonagemClasse.objects.all()
    serializer_class = PersonagemClasseSerializer
    http_method_names = ['post', 'patch']


class PersonagemModeloViewSet(ModelViewSet):
    """
    create:
        Adiciona um novo modelo a um personagem existente
    partial_update:
        Atualiza um ou mais campos de um modelo de um personagem existente
    """
    queryset = PersonagemModelo.objects.all()
    serializer_class = PersonagemModeloSerializer
    http_method_names = ['post', 'patch']


class PersonagemAtributoViewSet(ModelViewSet):
    """
    partial_update:
        Atualiza um ou mais campos de um atributo de um personagem existente
    """
    queryset = PersonagemAtributo.objects.all()
    serializer_class = PersonagemAtributoSerializer
    http_method_names = ['patch']
