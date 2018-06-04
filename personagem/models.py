from django.db.models import Model, ForeignKey, ManyToManyField, \
    CharField, IntegerField, FloatField, TextField, ImageField, \
    CASCADE, SET_NULL, PROTECT
from model_utils import Choices
from django.contrib.auth.models import User
from campanha.models import Arco
from core.models import Tendencia, Raca, Classe, Modelo
from .utils import get_personagem_upload_path


class Personagem(Model):
    jogador = ForeignKey(User, on_delete=CASCADE)
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
    tamanho = CharField(choices=TAMANHO, max_length=2)

    lore = TextField(null=True, blank=True)

    tendencia = ForeignKey(Tendencia, on_delete=PROTECT, related_name='+')
    raca = ForeignKey(Raca, on_delete=PROTECT, related_name='+')
    classes = ManyToManyField(
        Classe,
        through='PersonagemClasse',
        related_name='+'
    )
    modelos = ManyToManyField(Modelo, blank=True)

    def __str__(self):
        return self.nome

    @property
    def bba(self):
        print('getting bba')
        bba_atual = 0
        print('bba_atual: {}'.format(bba_atual))
        for personagem_classe in self.personagem_classes.all():
            print('personagem_classe: {}'.format(personagem_classe))
            print('bba do {}: {}'.format(personagem_classe, personagem_classe.get_bba()))
            bba_atual += personagem_classe.get_bba()
        return bba_atual

    class Meta:
        unique_together = ('jogador', 'nome')


class PersonagemClasse(Model):
    personagem = ForeignKey(Personagem, on_delete=CASCADE, related_name='personagem_classes')
    classe = ForeignKey(Classe, on_delete=PROTECT, related_name='+')
    nivel = IntegerField()

    def __str__(self):
        return '{} | {}'.format(self.personagem, self.classe)

    def get_bba(self):
        assert isinstance(self.classe, Classe)
        return self.classe.get_bba_nivel(self.nivel)

    class Meta:
        unique_together = ('personagem', 'classe')