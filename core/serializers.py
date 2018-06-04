from rest_framework.serializers import ModelSerializer
from rest_polymorphic.serializers import PolymorphicSerializer
from .models import Classe, ClassePrestigio


class ClasseSerializer(ModelSerializer):
    class Meta:
        model = Classe
        # fields = '__all__'
        exclude = ['polymorphic_ctype']
        # exclude = ['pericias', 'bbas', 'resistencias', 'tendencias']


class ClassePrestigioSerializer(ModelSerializer):
    class Meta:
        model = Classe
        # fields = '__all__'
        exclude = ['polymorphic_ctype']
        # exclude = ['pericias', 'bbas', 'resistencias', 'tendencias', 'dv']


class ClassePolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Classe: ClasseSerializer,
        ClassePrestigio: ClassePrestigioSerializer
    }
