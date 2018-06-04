from rest_framework.serializers import ModelSerializer, IntegerField, CharField, StringRelatedField
from .models import Personagem, PersonagemClasse, PersonagemModelo, PersonagemAtributo
from core.serializers import ClasseSerializer


class PersonagemClasseSerializer(ModelSerializer):
    # classe = ClasseSerializer(read_only=True)
    classe_nome = StringRelatedField(source='classe', read_only=True)

    class Meta:
        model = PersonagemClasse
        fields = '__all__'
        # exclude = ['personagem']


class PersonagemModeloSerializer(ModelSerializer):
    # classe = ClasseSerializer(read_only=True)
    modelo_nome = StringRelatedField(source='modelo', read_only=True)

    class Meta:
        model = PersonagemModelo
        fields = '__all__'
        # exclude = ['personagem']


class PersonagemAtributoSerializer(ModelSerializer):
    mod = CharField(read_only=True)
    nome = CharField(read_only=True)
    slug = CharField(read_only=True)

    class Meta:
        model = PersonagemAtributo
        # fields = '__all__'
        exclude = ['atributo', 'personagem']


class PersonagemSerializer(ModelSerializer):
    jodador_nome = StringRelatedField(source='jogador.first_name', read_only=True)
    arco_nome = StringRelatedField(source='arco', read_only=True)
    classes = PersonagemClasseSerializer(many=True, read_only=True)
    modelos = PersonagemModeloSerializer(many=True, read_only=True)
    atributos = PersonagemAtributoSerializer(many=True, read_only=True)
    bba = CharField(read_only=True)
    tendencia_nome = StringRelatedField(source='tendencia', read_only=True)
    raca_nome = StringRelatedField(source='raca', read_only=True)

    class Meta:
        model = Personagem
        exclude = ['lista_classes', 'lista_atributos', 'lista_modelos']
