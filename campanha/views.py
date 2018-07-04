from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from api.permissions import IsOwnerOrRead
from .models import Campanha, Arco
from .serializers import CampanhaSerializer, ArcoSerializer


class CampanhaViewSet(ModelViewSet):
    """
    retrieve:
        Retorna uma campanha
    list:
        Retorna todas as campanhas que o usuário mestra
    create:
        Cria uma nova campanha
    delete:
        Remove uma campanha existente
    partial_update:
        Atualiza um ou mais campos de uma campanha existente
    update:
        Atualiza uma campanha
    """
    permission_classes = [
        IsAuthenticated, IsOwnerOrRead
    ]
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def list(self, request, *args, **kwargs):
        campanhas = []
        for campanha in request.user.campanhas.all():
            if campanha not in campanhas:
                campanhas.append(campanha)
        headers = self.get_success_headers(self.serializer_class(campanhas, many=True).data)
        return Response(self.serializer_class(campanhas, many=True).data, status=HTTP_200_OK, headers=headers)

    @action(methods=['get'], detail=False)
    def jogando(self, request, *args, **kwargs):
        """
        Retorna todas as campanhas que o usuário está jogando
        """
        campanhas = []
        for personagem in request.user.personagens.all():
            if personagem.arco.campanha not in campanhas:
                campanhas.append(personagem.arco.campanha)
        headers = self.get_success_headers(self.serializer_class(campanhas, many=True).data)
        return Response(self.serializer_class(campanhas, many=True).data, status=HTTP_200_OK, headers=headers)


class ArcoViewSet(ModelViewSet):
    """
    retrieve:
        Retorna um arco
    list:
        Retorna todos os arcos do usuário
    create:
        Cria um novo arco
    delete:
        Remove um arco existente
    partial_update:
        Atualiza um ou mais campos de um arco existente
    update:
        Atualiza um arco
    """
    permission_classes = [
        IsAuthenticated, IsOwnerOrRead
    ]
    queryset = Arco.objects.all()
    serializer_class = ArcoSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def list(self, request, *args, **kwargs):
        arcos = []
        for personagem in request.user.personagens.all():
            if personagem.arco not in arcos:
                arcos.append(personagem.arco)
        headers = self.get_success_headers(self.serializer_class(arcos, many=True).data)
        return Response(self.serializer_class(arcos, many=True).data, status=HTTP_200_OK, headers=headers)
