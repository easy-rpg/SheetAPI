from django.db.models import Model, OneToOneField, ForeignKey, CharField, CASCADE, SET_NULL
from usuario.models import PerfilUsuario


class Campanha(Model):
    nome = CharField()
    mestre = ForeignKey(PerfilUsuario, on_delete=SET_NULL, related_name='campanhas')


class Arco(Model):
    nome = CharField()
    campanha = ForeignKey(Campanha, on_delete=CASCADE, related_name='arcos')
