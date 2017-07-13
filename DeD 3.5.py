from rpg.core.models import *
from rpg import db


classes = []
classes.append(Classe('Bárbaro'))
classes.append(Classe('Bardo'))
classes.append(Classe('Clérigo'))
classes.append(Classe('Druida'))
classes.append(Classe('Feiticeiro'))
classes.append(Classe('Guerreiro'))
classes.append(Classe('Ladino'))
classes.append(Classe('Mago'))
classes.append(Classe('Paladino'))
classes.append(Classe('Ranger'))
# classes.append(ClassePrestigio(''))
# classes.append(ClassePrestigio(''))
# classes.append(ClassePrestigio(''))
# classes.append(ClassePrestigio(''))
# classes.append(ClassePrestigio(''))
# classes.append(ClassePrestigio(''))
# classes.append(ClassePrestigio(''))
# classes.append(ClassePrestigio(''))
# classes.append(ClassePrestigio(''))


for classe in classes:
    db.session.add(classe)


db.session.commit()
