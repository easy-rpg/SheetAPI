from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Classe
from .serializers import ClassePolymorphicSerializer


class ClasseViewset(ModelViewSet):
    """
    retrieve:
        Retorna uma classe
    list:
        Retorna todas as classes
    """
    queryset = Classe.objects.all()
    serializer_class = ClassePolymorphicSerializer
    http_method_names = ['get']
