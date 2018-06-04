from rest_framework.viewsets import ModelViewSet
from .models import Classe
from .serializers import ClasseSerializer


class ClasseViewset(ModelViewSet):
    """
    retrieve:
        Retorna uma classe
    list:
        Retorna todas as classes
    """
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    http_method_names = ['get']
