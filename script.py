import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SheetAPI.settings")
django.setup()

from django.contrib.auth.models import User
from django.db import IntegrityError
from core.models import Atributo, Resistencia, Tendencia, Bba, Pericia, Classe, ClassePrestigio

for user in User.objects.all():
    print(user)

del(user)

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

del(nome)
del(atributo)

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

del(nome_resistencia)
del(nome_qualidade)
del(qualidade)
del(resistencia)
del(index)

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

del(nome)
del(tendencia)

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
            instancia = Bba(qualidade=qualidade, nivel=bbas[index]['nivel'], valor=bbas[index]['valor'])
            instancia.save()
            BBAS[qualidade][index]['instancia'] = instancia
        except IntegrityError as e:
            BBAS[qualidade][index]['instancia'] = Bba.objects.get(qualidade=qualidade, nivel=bbas[index]['nivel'], valor=bbas[index]['valor'])
            print(e)

del(qualidade)
del(bbas)
del(index)

PERICIAS = {
    'abrir_fechaduras': {'nome': 'Abrir Fechaduras', 'slug': 'abrir_fechaduras', 'atributo': ATRIBUTOS['destreza']['instancia']},
    'acrobacia': {'nome': 'Acrobacia', 'slug': 'acrobacia', 'atributo': ATRIBUTOS['destreza']['instancia']},
    'adestrar_animais': {'nome': 'Adestrar Animais', 'slug': 'adestrar_animais', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'arte_da_fuga': {'nome': 'Arte da Fuga', 'slug': 'arte_da_fuga', 'atributo': ATRIBUTOS['destreza']['instancia']},
    'atuacao_dramaturgia': {'nome': 'Atuação Dramaturgia', 'slug': 'atuacao_dramaturgia', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'atuacao_humor': {'nome': 'Atuação Humor', 'slug': 'atuacao_humor', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'atuacao_danca': {'nome': 'Atuação Dança', 'slug': 'atuacao_danca', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'atuacao_oratoria': {'nome': 'Atuação Oratoria', 'slug': 'atuacao_oratoria', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'atuacao_canto': {'nome': 'Atuação Canto', 'slug': 'atuacao_canto', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'atuacao_instrumentos_de_percussao': {'nome': 'Atuação Intrumentos de Percussão', 'slug': 'atuacao_instrumentos_de_percussao', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'atuacao_instrumentos_de_corda': {'nome': 'Atuação Intrumentos de Corda', 'slug': 'atuacaoinstrumentos_de_corda', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'atuacao_instrumentos_de_sopro': {'nome': 'Atuação Intrumentos de Sopro', 'slug': 'atuacao_instrumentos_de_sopro', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'atuacao_instrumentos_de_teclado': {'nome': 'Atuação Intrumentos de Teclado', 'slug': 'atuacao_instrumentos_de_teclado', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'avaliacao': {'nome': 'Avaliação', 'slug': 'avaliacao', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'blefar': {'nome': 'Blefar', 'slug': 'blefar', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'cavalgar': {'nome': 'Cavalgar', 'slug': 'cavalgar', 'atributo': ATRIBUTOS['destreza']['instancia']},
    'concentracao': {'nome': 'Concentração', 'slug': 'concentracao', 'atributo': ATRIBUTOS['constituicao']['instancia']},
    'conhecimento_arcano': {'nome': 'Conhecimento Arcano', 'slug': 'conhecimento_arcano', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'conhecimento_arquitetura_e_engenharia': {'nome': 'Conhecimento Arquitetura e Engenharia', 'slug': 'conhecimento_arquitetura_e_engenharia', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'conhecimento_masmorras': {'nome': 'Conhecimento Masmorras', 'slug': 'conhecimento_masmorras', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'conhecimento_geografia': {'nome': 'Conhecimento Geografia', 'slug': 'conhecimento_geografia', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'conhecimento_historia': {'nome': 'Conhecimento História', 'slug': 'conhecimento_historia', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'conhecimento_local': {'nome': 'Conhecimento Local', 'slug': 'conhecimento_local', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'conhecimento_natureza': {'nome': 'Conhecimento Natureza', 'slug': 'conhecimento_natureza', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'conhecimento_nobreza_e_realeza': {'nome': 'Conhecimento Nobreza e Realeza', 'slug': 'conhecimento_nobreza_e_realeza', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'conhecimento_religiao': {'nome': 'Conhecimento Religião', 'slug': 'conhecimento_religiao', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'conhecimento_planos': {'nome': 'Conhecimento Planos', 'slug': 'conhecimento_planos', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'cura': {'nome': 'Cura', 'slug': 'cura', 'atributo': ATRIBUTOS['sabedoria']['instancia']},
    'decrifrar_escrita': {'nome': 'Decrifrar Escrita', 'slug': 'decrifrar_escrita', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'diplomacia': {'nome': 'Diplomacia', 'slug': 'diplomacia', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'disfarce': {'nome': 'Disfarce', 'slug': 'disfarce', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'equilibrio': {'nome': 'Equilibrio', 'slug': 'equilibrio', 'atributo': ATRIBUTOS['destreza']['instancia']},
    'escalar': {'nome': 'Escalar', 'slug': 'escalar', 'atributo': ATRIBUTOS['forca']['instancia']},
    'esconder_se': {'nome': 'Esconder-se', 'slug': 'esconder_se', 'atributo': ATRIBUTOS['destreza']['instancia']},
    'falsificacao': {'nome': 'Falsificação', 'slug': 'falsificacao', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'furtividade': {'nome': 'Furtividade', 'slug': 'furtividade', 'atributo': ATRIBUTOS['destreza']['instancia']},
    'identificar_magia': {'nome': 'Identificar Magia', 'slug': 'identificar_magia', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'intimidar': {'nome': 'Intimidar', 'slug': 'intimidar', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'natacao': {'nome': 'Natação', 'slug': 'natacao', 'atributo': ATRIBUTOS['forca']['instancia']},
    'observar': {'nome': 'Observar', 'slug': 'observar', 'atributo': ATRIBUTOS['sabedoria']['instancia']},
    'obter_informacao': {'nome': 'Obter Informação', 'slug': 'obter_informacao', 'atributo': ATRIBUTOS['carisma']['instancia']},
    'oficio_alquimia': {'nome': 'Ofício Alquimia', 'slug': 'oficio_alquimia', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'oficio_armadilharia': {'nome': 'Ofício Armadilharia', 'slug': 'oficio_armadilharia', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'oficio_armeiro': {'nome': 'Ofício Armeiro', 'slug': 'oficio_armeiro', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'oficio_armoraria': {'nome': 'Ofício Amoraria', 'slug': 'oficio_armoraria', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'oficio_arquearia': {'nome': 'Ofício Arquearia', 'slug': 'oficio_arquearia', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'oficio_escultura': {'nome': 'Ofício Escultura', 'slug': 'oficio_escultura', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'oficio_pintura': {'nome': 'Ofício Pintura', 'slug': 'oficio_pintura', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'operar_mecanismo': {'nome': 'Operar Mecanismo', 'slug': 'operar_mecanismo', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'ouvir': {'nome': 'Ouvir', 'slug': 'ouvir', 'atributo': ATRIBUTOS['sabedoria']['instancia']},
    'procurar': {'nome': 'Procurar', 'slug': 'procurar', 'atributo': ATRIBUTOS['inteligencia']['instancia']},
    'prestidigitacao': {'nome': 'Prestidigitação', 'slug': 'prestidigitacao', 'atributo': ATRIBUTOS['destreza']['instancia']},
    'saltar': {'nome': 'Saltar', 'slug': 'saltar', 'atributo': ATRIBUTOS['forca']['instancia']},
    'sentir_motivacao': {'nome': 'Sentir Motivação', 'slug': 'sentir_motivacao', 'atributo': ATRIBUTOS['sabedoria']['instancia']},
    'sobrevivencia': {'nome': 'Sobrevivência', 'slug': 'sobrevivencia', 'atributo': ATRIBUTOS['sabedoria']['instancia']},
    'usar_cordas': {'nome': 'Usar Cordas', 'slug': 'usar_cordas', 'atributo': ATRIBUTOS['destreza']['instancia']},
    'usar_instrumento_magico': {'nome': 'Usar Instrumento Mágico', 'slug': 'usar_instrumento_magico', 'atributo': ATRIBUTOS['carisma']['instancia']}
}

for nome, pericia in PERICIAS.items():
    try:
        instancia = Pericia(nome=PERICIAS[nome]['nome'], slug=PERICIAS[nome]['slug'], atributo=PERICIAS[nome]['atributo'])
        instancia.save()
        PERICIAS[nome]['instancia'] = instancia
    except IntegrityError as e:
        PERICIAS[nome]['instancia'] = Pericia.objects.get(slug=PERICIAS[nome]['slug'])
        print(e)

del(nome)
del(pericia)

CLASSES = {
    'barbaro': {
        'nome': 'Bárbaro',
        'slug': 'barbaro',
        'dv': 12,
        'quantidade_pericias_por_nivel': 4,
        'conjurador': 'nan',
        'tendencias': [
            TENDENCIAS['NeB']['instancia'],
            TENDENCIAS['N']['instancia'],
            TENDENCIAS['NeM']['instancia'],
            TENDENCIAS['CeB']['instancia'],
            TENDENCIAS['CeN']['instancia'],
            TENDENCIAS['CeM']['instancia']
        ],
        'pericias_disponiveis': [
            PERICIAS['adestrar_animais']['instancia'],
            PERICIAS['cavalgar']['instancia'],
            PERICIAS['escalar']['instancia'],
            PERICIAS['intimidar']['instancia'],
            PERICIAS['natacao']['instancia'],
            PERICIAS['oficio_armadilharia']['instancia'],
            PERICIAS['oficio_armoraria']['instancia'],
            PERICIAS['oficio_arquearia']['instancia'],
            PERICIAS['oficio_armeiro']['instancia'],
            PERICIAS['oficio_escultura']['instancia'],
            PERICIAS['oficio_pintura']['instancia'],
            PERICIAS['ouvir']['instancia'],
            PERICIAS['saltar']['instancia'],
            PERICIAS['sobrevivencia']['instancia']
        ],
        'bbas': Bba.objects.filter(qualidade='boa'),
        'resistencias': Resistencia.objects.filter(slug='fort',qualidade='boa') |
            Resistencia.objects.filter(slug='ref',qualidade='ruim') |
            Resistencia.objects.filter(slug='von',qualidade='ruim')
    }
}

for nome, classe in CLASSES.items():
    try:
        instancia = Classe(nome=classe['nome'], slug=classe['slug'], dv=classe['dv'], conjurador=classe['conjurador'],
                           quantidade_pericias_por_nivel=classe['quantidade_pericias_por_nivel'])
        instancia.save()
        instancia.tendencias.set(classe['tendencias'])
        instancia.pericias_disponiveis.set(classe['pericias_disponiveis'])
        instancia.bbas.set(classe['bbas'])
        instancia.resistencias.set(classe['resistencias'])

        instancia.save()
        CLASSES[nome]['instancia'] = instancia
    except IntegrityError as e:
        CLASSES[nome]['instancia'] = Classe.objects.get(slug=classe['slug'])
        print(e)

del(nome)
del(classe)
del(instancia)

CLASSES_PRESTIGIO = {

}
