from django.db.models import Model, BooleanField, CharField, IntegerField, ManyToManyField, OneToOneField, ForeignKey, PROTECT
from django.core.validators import MaxValueValidator, MinValueValidator
from polymorphic.models import PolymorphicModel
from model_utils import Choices

# Create your models here.
class Tendencia(Model):
    valor = CharField()

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


class Atributo(Model):
    nome = CharField()
    slug = CharField()


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
    TIPO = Choices(('fort', ('Fortitude')), ('ref', ('Reflexo')), ('von', ('Vontade')))
    tipo = CharField(choices=TIPO, max_length=4)
    QUALIDADE = Choices(('boa', ('Resistencia Boa')), ('ruim', ('Resistencia Ruim')))
    qualidade = CharField(choices=QUALIDADE, max_length=4)
    atributo = OneToOneField(Atributo, related_name='+')


class Pericia(Model):
    nome = CharField()
    slug = CharField()
    # ATRIBUTO = Choices(('for', ('Força')), ('des', ('Destreza')), ('con', ('Constituição')),
    #                   ('int', ('Inteligência')), ('sab', ('Sabedoria')), ('car', ('Carisma')))
    # atributo = CharField(choices=ATRIBUTO, max_length=3)
    atributo = ForeignKey(Atributo, related_name='+', on_delete=PROTECT)


class Classe(PolymorphicModel):
    nome = CharField()
    pericias_disponiveis = ManyToManyField(Pericia, related_name='+')
    quantidade_pericias_por_nivel = IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    BBAs = ManyToManyField(BBA, related_name='+')
    tendencias = ManyToManyField(Tendencia, related_name='+')
    DV = Choices((4, ('d4')), (6, ('d6')),(8, ('d8')), (10, ('d10')), (12, ('d12')))
    dv = IntegerField(choices=DV, max_length=2)
    CONJURADOR = Choices(('div', ('Divino')), ('arc', ('Arcano')), ('nan', ('Não conjurador')))
    conjurador = CharField(choices=CONJURADOR, default=CONJURADOR.nan, max_length=3)
    # conjurador_completo = BooleanField(default=True)

class ClassePrestigio(Classe):
    pass