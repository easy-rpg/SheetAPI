from django.db.models import Model, ForeignKey, ManyToManyField, \
    CharField, IntegerField, FloatField, TextField, ImageField, \
    CASCADE, SET_NULL, PROTECT
from django.db.models.signals import post_save
from model_utils import Choices
from django.contrib.auth.models import User
from campanha.models import Arco
from core.models import Atributo, Tendencia, Raca, Classe, Modelo
from .utils import get_personagem_upload_path


class Personagem(Model):
    jogador = ForeignKey(User, on_delete=CASCADE, related_name='personagens')
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

    lista_atributos = ManyToManyField(
        Atributo,
        through='PersonagemAtributo',
        related_name='+'
    )
    tendencia = ForeignKey(Tendencia, on_delete=PROTECT, related_name='+')
    raca = ForeignKey(Raca, on_delete=PROTECT, related_name='+')
    lista_classes = ManyToManyField(
        Classe,
        through='PersonagemClasse',
        related_name='+'
    )
    lista_modelos = ManyToManyField(
        Modelo,
        through='PersonagemModelo',
        related_name='+',
        blank=True
    )

    def __str__(self):
        return self.nome

    @property
    def owner(self):
        return self.jogador

    @property
    def bba(self):
        # print('getting bba')
        bba_atual = 0
        # print('bba_atual: {}'.format(bba_atual))
        for classe in self.classes.all():
            # print('personagem_classe: {}'.format(classe))
            # print('bba do {}: {}'.format(classe, classe.get_bba()))
            bba_atual += classe.get_bba()
        return '+{}'.format(bba_atual)

    class Meta:
        unique_together = ('jogador', 'nome')


class PersonagemClasse(Model):
    personagem = ForeignKey(Personagem, on_delete=CASCADE, related_name='classes')
    classe = ForeignKey(Classe, on_delete=PROTECT, related_name='+')
    nivel = IntegerField()

    def __str__(self):
        return '{} | {}'.format(self.personagem, self.classe)

    @property
    def owner(self):
        return self.personagem.jogador

    def get_bba(self):
        assert isinstance(self.classe, Classe)
        return self.classe.get_bba_nivel(self.nivel)

    class Meta:
        unique_together = ('personagem', 'classe')


class PersonagemModelo(Model):
    personagem = ForeignKey(Personagem, on_delete=CASCADE, related_name='modelos')
    modelo = ForeignKey(Modelo, on_delete=PROTECT, related_name='+')

    def __str__(self):
        return '{} | {}'.format(self.personagem, self.modelo)

    @property
    def owner(self):
        return self.personagem.jogador

    @property
    def nome(self):
        return self.modelo.nome

    class Meta:
        unique_together = ('personagem', 'modelo')


class PersonagemAtributo(Model):
    personagem = ForeignKey(Personagem, on_delete=CASCADE, related_name='atributos')
    atributo = ForeignKey(Atributo, on_delete=PROTECT, related_name='+')
    valor = IntegerField(default=0)
    valor_temporario = IntegerField(default=0)

    def __str__(self):
        return self.nome

    @property
    def owner(self):
        return self.personagem.jogador

    @property
    def mod(self):
        mod = self.valor + self.valor_temporario
        if mod%2 == 1:
            mod -= 1
        return '+{}'.format(int((mod-10)/2))

    @property
    def nome(self):
        return self.atributo.nome

    @property
    def slug(self):
        return self.atributo.slug

    class Meta:
        unique_together = ('personagem', 'atributo')

def add_atributos(sender, **kwargs):
    personagem = kwargs["instance"]
    if kwargs["created"]:
        atributos = Atributo.objects.all()
        for atributo in atributos:
            PersonagemAtributo(personagem=personagem, atributo=atributo).save()

post_save.connect(add_atributos, sender=Personagem)