from rpg.core.models import *
from rpg import db


classes = []
# classes.append(Classe('Bárbaro'))
# classes.append(Classe('Bardo'))
# classes.append(Classe('Clérigo'))
# classes.append(Classe('Druida'))
# classes.append(Classe('Feiticeiro'))
# classes.append(Classe('Guerreiro'))
# classes.append(Classe('Ladino'))
# classes.append(Classe('Mago'))
# classes.append(Classe('Paladino'))
# classes.append(Classe('Ranger'))
# classes.append(ClassePrestigio('Algoz', 10))
# classes.append(ClassePrestigio('Assassino das Sombras', 10))
# classes.append(ClassePrestigio('Bardo Dracônico', 5))
# classes.append(ClassePrestigio('Bárbaro Frenético', 10))
# classes.append(ClassePrestigio('Caçador', 5))
# classes.append(ClassePrestigio('Devoto da Guerra', 10))
# classes.append(ClassePrestigio('Encantatriz', 10))
# classes.append(ClassePrestigio('Hierofante', 10))
# classes.append(ClassePrestigio('Kensai', 10))
# classes.append(ClassePrestigio('Mestre das Mortalhas', 10))
# classes.append(ClassePrestigio('Metamorfo de Guerra', 5))
# classes.append(ClassePrestigio('Monge Tatuado', 10))
# classes.append(ClassePrestigio('Transmorfo', 10))

# classes.append(ClassePrestigio('', ))


for classe in classes:
    db.session.add(classe)


db.session.commit()
