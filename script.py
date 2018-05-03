import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SheetAPI.settings")
django.setup()

from django.contrib.auth.models import User
from django.db import IntegrityError
from core.models import Atributo, Resistencia, Tendencia, BBA

users = User.objects.all()
for user in users:
    print(user)

rodrigo = User(username='rodrigondec', email='rodrigondec@gmail.com',
               password='pbkdf2_sha256$100000$fQgW32ScWiVI$n3psZOWZvSqL8154DXXEBlRxpr1r57f6ANQSnF+qPU8=',
               is_staff=True, is_superuser=True)
try:
    rodrigo.save()
except IntegrityError as e:
    rodrigo = User.objects.get(username='rodrigondec')
    print(e)


ATRIBUTOS = {
    'forca': {'nome': 'Força', 'slug': 'for'},
    'destreza': {'nome': 'Destreza', 'slug': 'des'},
    'constituicao': {'nome': 'Constituição', 'slug': 'con'},
    'inteligencia': {'nome': 'Inteligência', 'slug': 'int'},
    'sabedoria': {'nome': 'Sabedoria', 'slug': 'sab'},
    'carisma': {'nome': 'Carisma', 'slug': 'car'}
}

for nome, atributo in ATRIBUTOS.items():
    try:
        instancia = Atributo(nome=atributo['nome'], slug=atributo['slug'])
        instancia.save()
        ATRIBUTOS[nome]['instancia'] = instancia
    except IntegrityError as e:
        ATRIBUTOS[nome]['instancia'] = Atributo.objects.get(slug=atributo['slug'])
        print(e)


RESISTENCIAS = {
    'fortitude': {'nome': 'Fortitude', 'slug': 'fort', 'atributo': ATRIBUTOS['constituicao']['instancia'], 'qualidades': {
        'boa': [
            {'nivel': 1, 'valor': 2},
            {'nivel': 2, 'valor': 3},
            {'nivel': 3, 'valor': 3},
            {'nivel': 4, 'valor': 4},
            {'nivel': 5, 'valor': 4},
            {'nivel': 6, 'valor': 5},
            {'nivel': 7, 'valor': 5},
            {'nivel': 8, 'valor': 6},
            {'nivel': 9, 'valor': 6},
            {'nivel': 10, 'valor': 7},
            {'nivel': 11, 'valor': 7},
            {'nivel': 12, 'valor': 8},
            {'nivel': 13, 'valor': 8},
            {'nivel': 14, 'valor': 9},
            {'nivel': 15, 'valor': 9},
            {'nivel': 16, 'valor': 10},
            {'nivel': 17, 'valor': 10},
            {'nivel': 18, 'valor': 11},
            {'nivel': 19, 'valor': 11},
            {'nivel': 20, 'valor': 12}
        ],
        'ruim': [
            {'nivel': 1, 'valor': 0},
            {'nivel': 2, 'valor': 0},
            {'nivel': 3, 'valor': 1},
            {'nivel': 4, 'valor': 1},
            {'nivel': 5, 'valor': 1},
            {'nivel': 6, 'valor': 2},
            {'nivel': 7, 'valor': 2},
            {'nivel': 8, 'valor': 2},
            {'nivel': 9, 'valor': 3},
            {'nivel': 10, 'valor': 3},
            {'nivel': 11, 'valor': 3},
            {'nivel': 12, 'valor': 4},
            {'nivel': 13, 'valor': 4},
            {'nivel': 14, 'valor': 4},
            {'nivel': 15, 'valor': 5},
            {'nivel': 16, 'valor': 5},
            {'nivel': 17, 'valor': 5},
            {'nivel': 18, 'valor': 6},
            {'nivel': 19, 'valor': 6},
            {'nivel': 20, 'valor': 6}
        ]
    }},
    'reflexos': {'nome': 'Reflexos', 'slug': 'ref', 'atributo': ATRIBUTOS['destreza']['instancia'], 'qualidades': {
        'boa': [
            {'nivel': 1, 'valor': 2},
            {'nivel': 2, 'valor': 3},
            {'nivel': 3, 'valor': 3},
            {'nivel': 4, 'valor': 4},
            {'nivel': 5, 'valor': 4},
            {'nivel': 6, 'valor': 5},
            {'nivel': 7, 'valor': 5},
            {'nivel': 8, 'valor': 6},
            {'nivel': 9, 'valor': 6},
            {'nivel': 10, 'valor': 7},
            {'nivel': 11, 'valor': 7},
            {'nivel': 12, 'valor': 8},
            {'nivel': 13, 'valor': 8},
            {'nivel': 14, 'valor': 9},
            {'nivel': 15, 'valor': 9},
            {'nivel': 16, 'valor': 10},
            {'nivel': 17, 'valor': 10},
            {'nivel': 18, 'valor': 11},
            {'nivel': 19, 'valor': 11},
            {'nivel': 20, 'valor': 12}
        ],
        'ruim': [
            {'nivel': 1, 'valor': 0},
            {'nivel': 2, 'valor': 0},
            {'nivel': 3, 'valor': 1},
            {'nivel': 4, 'valor': 1},
            {'nivel': 5, 'valor': 1},
            {'nivel': 6, 'valor': 2},
            {'nivel': 7, 'valor': 2},
            {'nivel': 8, 'valor': 2},
            {'nivel': 9, 'valor': 3},
            {'nivel': 10, 'valor': 3},
            {'nivel': 11, 'valor': 3},
            {'nivel': 12, 'valor': 4},
            {'nivel': 13, 'valor': 4},
            {'nivel': 14, 'valor': 4},
            {'nivel': 15, 'valor': 5},
            {'nivel': 16, 'valor': 5},
            {'nivel': 17, 'valor': 5},
            {'nivel': 18, 'valor': 6},
            {'nivel': 19, 'valor': 6},
            {'nivel': 20, 'valor': 6}
        ]
    }},
    'vontade': {'nome': 'Vontade', 'slug': 'von', 'atributo': ATRIBUTOS['sabedoria']['instancia'], 'qualidades': {
        'boa': [
            {'nivel': 1, 'valor': 2},
            {'nivel': 2, 'valor': 3},
            {'nivel': 3, 'valor': 3},
            {'nivel': 4, 'valor': 4},
            {'nivel': 5, 'valor': 4},
            {'nivel': 6, 'valor': 5},
            {'nivel': 7, 'valor': 5},
            {'nivel': 8, 'valor': 6},
            {'nivel': 9, 'valor': 6},
            {'nivel': 10, 'valor': 7},
            {'nivel': 11, 'valor': 7},
            {'nivel': 12, 'valor': 8},
            {'nivel': 13, 'valor': 8},
            {'nivel': 14, 'valor': 9},
            {'nivel': 15, 'valor': 9},
            {'nivel': 16, 'valor': 10},
            {'nivel': 17, 'valor': 10},
            {'nivel': 18, 'valor': 11},
            {'nivel': 19, 'valor': 11},
            {'nivel': 20, 'valor': 12}
        ],
        'ruim': [
            {'nivel': 1, 'valor': 0},
            {'nivel': 2, 'valor': 0},
            {'nivel': 3, 'valor': 1},
            {'nivel': 4, 'valor': 1},
            {'nivel': 5, 'valor': 1},
            {'nivel': 6, 'valor': 2},
            {'nivel': 7, 'valor': 2},
            {'nivel': 8, 'valor': 2},
            {'nivel': 9, 'valor': 3},
            {'nivel': 10, 'valor': 3},
            {'nivel': 11, 'valor': 3},
            {'nivel': 12, 'valor': 4},
            {'nivel': 13, 'valor': 4},
            {'nivel': 14, 'valor': 4},
            {'nivel': 15, 'valor': 5},
            {'nivel': 16, 'valor': 5},
            {'nivel': 17, 'valor': 5},
            {'nivel': 18, 'valor': 6},
            {'nivel': 19, 'valor': 6},
            {'nivel': 20, 'valor': 6}
        ]
    }}
}

for nome_resistencia, resistencia in RESISTENCIAS.items():
    for nome_qualidade, qualidade in resistencia['qualidades'].items():
        for index in range(0, len(qualidade)):
            # print(index)
            try:
                instancia = Resistencia(nome=resistencia['nome'], slug=resistencia['slug'],
                                        atributo=resistencia['atributo'], qualidade=nome_qualidade,
                                        nivel=qualidade[index]['nivel'], valor=qualidade[index]['valor'])
                instancia.save()
                RESISTENCIAS[nome_resistencia]['qualidades'][nome_qualidade][index]['instancia'] = instancia
            except IntegrityError as e:
                RESISTENCIAS[nome_resistencia]['qualidades'][nome_qualidade][index]['instancia'] = Resistencia.objects.get(slug=resistencia['slug'],
                                                                                                                           qualidade=nome_qualidade,
                                                                                                                           nivel=qualidade[index]['nivel'],
                                                                                                                           valor=qualidade[index]['valor'])
                print(e)


TENDENCIAS = {
    'LeB': {'valor': 'Leal e Bom', 'slug': 'LeB'},
    'LeN': {'valor': 'Leal e Neutro', 'slug': 'LeN'},
    'LeM': {'valor': 'Leal e Mal', 'slug': 'LeM'},
    'NeB': {'valor': 'Neutro e Bom', 'slug': 'NeB'},
    'N': {'valor': 'Neutro', 'slug': 'N'},
    'NeM': {'valor': 'Neutro e Mal', 'slug': 'NeM'},
    'CeB': {'valor': 'Caótico e Bom', 'slug': 'CeB'},
    'CeN': {'valor': 'Caótico e Neutro', 'slug': 'CeN'},
    'CeM': {'valor': 'Caótico e Mal', 'slug': 'CeM'}
}

for nome, tendencia in TENDENCIAS.items():
    try:
        instancia = Tendencia(valor=TENDENCIAS[nome]['valor'], slug=TENDENCIAS[nome]['slug'])
        instancia.save()
        TENDENCIAS[nome]['instancia'] = instancia
    except IntegrityError as e:
        TENDENCIAS[nome]['instancia'] = Tendencia.objects.get(slug=TENDENCIAS[nome]['slug'])
        print(e)

BBAS = {
    'boa': [
        {'nivel': 1, 'valor': 1},
        {'nivel': 2, 'valor': 2},
        {'nivel': 3, 'valor': 3},
        {'nivel': 4, 'valor': 4},
        {'nivel': 5, 'valor': 5},
        {'nivel': 6, 'valor': 6},
        {'nivel': 7, 'valor': 7},
        {'nivel': 8, 'valor': 8},
        {'nivel': 9, 'valor': 9},
        {'nivel': 10, 'valor': 10},
        {'nivel': 11, 'valor': 11},
        {'nivel': 12, 'valor': 12},
        {'nivel': 13, 'valor': 13},
        {'nivel': 14, 'valor': 14},
        {'nivel': 15, 'valor': 15},
        {'nivel': 16, 'valor': 16},
        {'nivel': 17, 'valor': 17},
        {'nivel': 18, 'valor': 18},
        {'nivel': 19, 'valor': 19},
        {'nivel': 20, 'valor': 20}
    ],
    'ruim': [
        {'nivel': 1, 'valor': 0},
        {'nivel': 2, 'valor': 1},
        {'nivel': 3, 'valor': 2},
        {'nivel': 4, 'valor': 3},
        {'nivel': 5, 'valor': 3},
        {'nivel': 6, 'valor': 4},
        {'nivel': 7, 'valor': 5},
        {'nivel': 8, 'valor': 6},
        {'nivel': 9, 'valor': 6},
        {'nivel': 10, 'valor': 7},
        {'nivel': 11, 'valor': 8},
        {'nivel': 12, 'valor': 9},
        {'nivel': 13, 'valor': 9},
        {'nivel': 14, 'valor': 10},
        {'nivel': 15, 'valor': 11},
        {'nivel': 16, 'valor': 12},
        {'nivel': 17, 'valor': 12},
        {'nivel': 18, 'valor': 13},
        {'nivel': 19, 'valor': 14},
        {'nivel': 20, 'valor': 15}
    ]
}

for qualidade, bbas in BBAS.items():
    for index in range(0, len(bbas)):

        try:
            instancia = BBA(qualidade=qualidade, nivel=bbas[index]['nivel'], valor=bbas[index]['valor'])
            instancia.save()
            BBAS[qualidade][index]['instancia'] = instancia
        except IntegrityError as e:
            BBAS[qualidade][index]['instancia'] = BBA.objects.get(qualidade=qualidade, nivel=bbas[index]['nivel'], valor=bbas[index]['valor'])
            print(e)

