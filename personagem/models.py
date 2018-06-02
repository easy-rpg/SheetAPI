from django.db.models import Model, OneToOneField, ForeignKey, ManyToManyField, \
    CharField, IntegerField, FloatField, TextField, ImageField, \
    CASCADE, SET_NULL, PROTECT
from model_utils import Choices
from usuario.models import PerfilUsuario
from campanha.models import Arco
from core.models import Tendencia, Raca, Classe, Subtipo, Modelo
from .utils import get_personagem_upload_path


class Ficha(Model):
    tendencia = ForeignKey(Tendencia, on_delete=PROTECT, related_name='+')
    raca = ForeignKey(Raca, on_delete=PROTECT, related_name='+')
    classes = ManyToManyField(Classe)
    sub_tipo = ForeignKey(Subtipo, on_delete=PROTECT, related_name='+')
    modelo = ForeignKey(Modelo, on_delete=PROTECT, related_name='+')


class Personagem(Model):
    usuario = ForeignKey(PerfilUsuario, on_delete=CASCADE)
    ficha = OneToOneField(Ficha, on_delete=CASCADE, related_name='+')
    arco = ForeignKey(Arco, on_delete=SET_NULL, null=True, related_name='personagens')
    nome = CharField(max_length=30, null=True, blank=True)
    foto = ImageField(upload_to=get_personagem_upload_path, null=True, blank=True)
    pele = CharField(max_length=10, null=True, blank=True)
    cabelos = CharField(max_length=10, null=True, blank=True)
    olhos = CharField(max_length=10, null=True, blank=True)
    peso = IntegerField(null=True, blank=True)
    altura = FloatField(null=True, blank=True)
    idade = IntegerField(null=True, blank=True)

    SEXO = Choices(('m', ('Masculino')), ('f', ('Feminino')))
    sexo = CharField(choices=SEXO, max_length=1)
    TAMANHO = Choices(('mi', ('Minúsculo')), ('di', ('Diminuto')), ('mu', ('Miúdo')),
                      ('pe', ('Pequeno')), ('me', ('Médio')), ('gr', ('Grande')),
                      ('en', ('Enorme')), ('im', ('Imenso')), ('co', ('Colossal')))
    tamanho = CharField(choices=SEXO, max_length=2)

    lore = TextField(null=True, blank=True)
