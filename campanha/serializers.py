from rest_framework.serializers import ModelSerializer, CharField
from .models import Campanha, Arco


class ArcoSerializer(ModelSerializer):
    campanha_nome = CharField(source='campanha.nome', read_only=True)
    class Meta:
        model = Arco
        fields = '__all__'


class CampanhaSerializer(ModelSerializer):
    arcos = ArcoSerializer(many=True, read_only=True)
    class Meta:
        model = Campanha
        fields = '__all__'
