from rest_framework.serializers import ModelSerializer, CharField, StringRelatedField
from .models import Campanha, Arco


class ArcoSerializer(ModelSerializer):
    campanha_nome = CharField(source='campanha.nome', read_only=True)
    personagens = StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Arco
        fields = '__all__'


class CampanhaSerializer(ModelSerializer):
    arcos = ArcoSerializer(many=True, read_only=True)
    mestre_nome = CharField(source='mestre.username', read_only=True)

    class Meta:
        model = Campanha
        fields = '__all__'
