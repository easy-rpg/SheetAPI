from rpg.core.models import *
from rpg import db

# rodrigo = Usuario(nome='Rodrigo', email='rodrigondec@gmail.com', senha='rodrigo123')
rodrigo = Usuario.query.filter_by(email='rodrigondec@gmail.com').first()
# db.session.add(rodrigo)
#
# clara = Usuario(nome='Clara', email='claranobre@gmail.com', senha='clara123')
clara = Usuario.query.filter_by(email='claranobre@gmail.com').first()
# db.session.add(clara)

file = Campanha(nome='Campanha do Filé')
# file = Campanha.query.filter_by(id_campanha=1).first()
db.session.add(file)

p = Participacao('Mestre')
p.usuario = rodrigo
p.campanha = file
db.session.add(p)
p2 = Participacao('Jogador')
p2.usuario = clara
p2.campanha = file
db.session.add(p2)

mesa_file_1 = Mesa(nome='Mesa 1')
# mesa_file_1 = Mesa.query.filter_by(id_mesa=1).first()
mesa_file_1.campanha = file
#
mesa_file_2 = Mesa(nome='Mesa 2')
# mesa_file_2 = Mesa.query.filter_by(id_mesa=2).first()
mesa_file_2.campanha = file
#
hieriling = Personagem(nome='Hieriling')
hieriling.usuario = rodrigo
hieriling.raca = Raca.query.filter_by(nome="Anão").first()
hieriling.classes.append(InstanciaClasse(Classe.query.filter_by(nome="Clérigo").first(), 5))
hieriling.classes.append(InstanciaClasse(Classe.query.filter_by(nome="Devoto da Guerra").first(), 8))
hieriling.mesa = mesa_file_1

assis = Personagem(nome='Assis')
assis.usuario = rodrigo
assis.raca = Raca.query.filter_by(nome='Anão').first()
assis.classes.append(InstanciaClasse(Classe.query.filter_by(nome='Bárbaro').first(), 6))
assis.classes.append(InstanciaClasse(Classe.query.filter_by(nome='Bárbaro Frenético').first(), 3))
assis.mesa = mesa_file_2

db.session.commit()
