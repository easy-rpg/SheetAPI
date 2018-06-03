from django.db.models import Model, OneToOneField, ForeignKey, CharField, CASCADE, SET_NULL
from usuario.models import PerfilUsuario


class Campanha(Model):
    nome = CharField(max_length=30, unique=True)
    mestre = ForeignKey(PerfilUsuario, on_delete=SET_NULL, null=True, related_name='campanhas')

    def __str__(self):
        return self.nome


class Arco(Model):
    nome = CharField(max_length=30, unique=True)
    campanha = ForeignKey(Campanha, on_delete=CASCADE, related_name='arcos')

    def __str__(self):
        return '{} | {}'.format(self.campanha, self.nome)
