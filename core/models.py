from django.db.models import Model, BooleanField, CharField, IntegerField, ManyToManyField, OneToOneField, ForeignKey, PROTECT
from django.core.validators import MaxValueValidator, MinValueValidator
from polymorphic.models import PolymorphicModel
from model_utils import Choices

# Create your models here.
class Tendencia(Model):
    valor = CharField(max_length=16, unique=True)
    slug = CharField(max_length=3, unique=True)

    def __str__(self):
        return self.valor

class BBA(Model):
    nivel = IntegerField(
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ]
    )
    valor = IntegerField(
        validators=[
            MaxValueValidator(20),
            MinValueValidator(0)
        ]
    )
    QUALIDADE = Choices(('boa', ('BBA Boa')), ('ruim', ('BBA Ruim')))
    qualidade = CharField(choices=QUALIDADE, max_length=4)

    class Meta:
        unique_together = ('qualidade', 'nivel', 'valor')

    def __str__(self):
        return 'BBA {} nível {}'.format(self.qualidade, self.nivel)

class Atributo(Model):
    NOME = Choices(('Força'), ('Destreza'), ('Constituição'),
                      ('Inteligência'), ('Sabedoria'), ('Carisma'))
    nome = CharField(choices=NOME, max_length=12, unique=True)
    SLUG = Choices(('for'), ('des'), ('con'),
                      ('int'), ('sab'), ('car'))
    slug = CharField(choices=SLUG, max_length=3, unique=True)

    def __str__(self):
        return self.nome

class Resistencia(Model):
    nivel = IntegerField(
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ]
    )
    valor = IntegerField(
        validators=[
            MaxValueValidator(20),
            MinValueValidator(0)
        ]
    )
    NOME =Choices(('Fortitude'), ('Reflexo'), ('Vontade'))
    nome = CharField(choices=NOME, max_length=9)
    SLUG = Choices(('fort'), ('ref'), ('von'))
    slug = CharField(choices=SLUG, max_length=4)
    QUALIDADE = Choices(('boa', ('Resistencia Boa')), ('ruim', ('Resistencia Ruim')))
    qualidade = CharField(choices=QUALIDADE, max_length=4)
    atributo = ForeignKey(Atributo, related_name='+', on_delete=PROTECT)

    class Meta:
        unique_together = ('slug', 'qualidade', 'nivel', 'valor')

    def __str__(self):
        return '{} {} nivel {}'.format(self.nome, self.qualidade, self.nivel)

class Pericia(Model):
    nome = CharField(max_length=24)
    slug = CharField(max_length=24)
    atributo = ForeignKey(Atributo, related_name='+', on_delete=PROTECT)

    def __str__(self):
        return self.nome


class Classe(PolymorphicModel):
    nome = CharField(max_length=20)
    pericias_disponiveis = ManyToManyField(Pericia, related_name='+')
    quantidade_pericias_por_nivel = IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    BBAs = ManyToManyField(BBA, related_name='+')
    tendencias = ManyToManyField(Tendencia, related_name='+')
    DV = Choices((4, ('d4')), (6, ('d6')),(8, ('d8')), (10, ('d10')), (12, ('d12')))
    dv = IntegerField(choices=DV)
    CONJURADOR = Choices(('div', ('Divino')), ('arc', ('Arcano')), ('nan', ('Não conjurador')))
    conjurador = CharField(choices=CONJURADOR, default=CONJURADOR.nan, max_length=3)
    # conjurador_completo = BooleanField(default=True)

class ClassePrestigio(Classe):
    pass