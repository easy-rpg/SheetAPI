from django.db.models import Model, OneToOneField, ForeignKey, \
    CharField, IntegerField, FloatField, TextField, ImageField, \
    CASCADE, SET_NULL, PROTECT
from usuario.models import PerfilUsuario
from campanha.models import Arco
from core.models import Tendencia,
from .utils import get_personagem_upload_path


class Ficha(Model):
    pass


class Personagem(Model):
    usuario = ForeignKey(PerfilUsuario, on_delete=CASCADE)
    ficha = OneToOneField(Ficha, on_delete=CASCADE, related_name='+')
    arco = ForeignKey(Arco, on_delete=SET_NULL, related_name='personagens')
    nome = CharField()
    foto = ImageField(upload_to=get_personagem_upload_path, null=True, blank=True)
    pele = CharField()
    cabelos = CharField()
    olhos = CharField()
    peso = IntegerField()
    altura = FloatField()
    idade = IntegerField()

    # sexo =
    # tamanho =
    lore = TextField()

    tendencia = ForeignKey(Tendencia, on_delete=PROTECT, related_name='+')
    raça = ForeignKey()
