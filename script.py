from rpg.core.models import *
from rpg import db

# rodrigo = Usuario(nome='Rodrigo', email='rodrigondec@gmail.com', senha='rodrigo123')
rodrigo = Usuario.query.filber_by(email='rodrigondec@gmail.com').first()
# db.session.add(rodrigo)





db.session.commit()
