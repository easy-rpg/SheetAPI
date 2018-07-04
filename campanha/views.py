from rest_framework.viewsets import ModelViewSet
from .models import Campanha, Arco
from .serializers import CampanhaSerializer, ArcoSerializer

class CampanhaViewSet(ModelViewSet):
    """
    retrieve:
        Retorna uma campanha
    list:
        Retorna todas as campanhas do usuário
    create:
        Cria uma nova campanha
    delete:
        Remove uma campanha existente
    partial_update:
        Atualiza um ou mais campos de uma campanha existente
    update:
        Atualiza uma campanha
    """
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    # def list(self, request, *args, **kwargs):



class ArcoViewSet(ModelViewSet):
    """
    retrieve:
        Retorna um arco
    list:
        Retorna todos os arcos
    create:
        Cria um novo arco
    delete:
        Remove um arco existente
    partial_update:
        Atualiza um ou mais campos de um arco existente
    update:
        Atualiza um arco
    """
    queryset = Arco.objects.all()
    serializer_class = ArcoSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
