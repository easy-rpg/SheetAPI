from django.db.models import Model, ForeignKey, CharField, CASCADE, SET_NULL
from django.contrib.auth.models import User


class Campanha(Model):
    nome = CharField(max_length=30, unique=True)
    mestre = ForeignKey(User, on_delete=SET_NULL, null=True, related_name='campanhas')

    def __str__(self):
        return self.nome

    @property
    def owner(self):
        return self.mestre


class Arco(Model):
    nome = CharField(max_length=30, unique=True)
    campanha = ForeignKey(Campanha, on_delete=CASCADE, related_name='arcos')

    def __str__(self):
        return '{} | {}'.format(self.campanha, self.nome)

    @property
    def owner(self):
        return self.campanha.mestre
