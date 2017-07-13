from rpg.core.models import *
from rpg import db

rodrigo = Usuario(nome='Rodrigo', email='rodrigondec@gmail.com', senha='rodrigo123')
db.session.add(rodrigo)





db.session.commit()
