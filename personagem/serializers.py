from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Personagem, PersonagemClasse
from core.serializers import ClasseSerializer


class PersonagemClasseSerializer(ModelSerializer):
    classe = ClasseSerializer(read_only=True)

    class Meta:
        model = PersonagemClasse
        fields = '__all__'


class PersonagemSerializer(ModelSerializer):
    personagem_classes = PersonagemClasseSerializer(many=True, read_only=True)
    bba = IntegerField()

    class Meta:
        model = Personagem
        fields = '__all__'
