from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from api.permissions import IsOwner
from .models import Personagem, PersonagemClasse, PersonagemModelo, PersonagemAtributo
from .serializers import PersonagemSerializer, PersonagemClasseSerializer, PersonagemModeloSerializer, \
    PersonagemAtributoSerializer


class PersonagemViewSet(ModelViewSet):
    """
    retrieve:
        Retorna um personagem
    list:
        Retorna todos os personagens do usuário
    create:
        Cria um novo personagem
    delete:
        Remove um personagem existente
    partial_update:
        Atualiza um ou mais campos de um personagem existente
    update:
        Atualiza um personagem
    """
    permission_classes = [
        IsAuthenticated, IsOwner
    ]
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.user.personagens, many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_200_OK, headers=headers)


class PersonagemClasseViewSet(ModelViewSet):
    """
    create:
        Adiciona uma nova classe a um personagem existente
    partial_update:
        Atualiza um ou mais campos de uma classe de um personagem existente
    """
    permission_classes = [
        IsAuthenticated, IsOwner
    ]
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
    permission_classes = [
        IsAuthenticated, IsOwner
    ]
    queryset = PersonagemModelo.objects.all()
    serializer_class = PersonagemModeloSerializer
    http_method_names = ['post', 'patch']


class PersonagemAtributoViewSet(ModelViewSet):
    """
    partial_update:
        Atualiza um ou mais campos de um atributo de um personagem existente
    """
    permission_classes = [
        IsAuthenticated, IsOwner
    ]
    queryset = PersonagemAtributo.objects.all()
    serializer_class = PersonagemAtributoSerializer
    http_method_names = ['patch']
