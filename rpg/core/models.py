from rpg import db
from sqlalchemy_utils import EmailType, PasswordType


campanha_mestres = db.Table(
    'campanha_mestres',
    db.Column('id_campanha', db.Integer, db.ForeignKey('campanha.id_campanha')),
    db.Column('id_usuario', db.Integer, db.ForeignKey('usuario.id_usuario'))
)


campanha_jogadores = db.Table(
    'campanha_jogadores',
    db.Column('id_campanha', db.Integer, db.ForeignKey('campanha.id_campanha')),
    db.Column('id_usuario', db.Integer, db.ForeignKey('usuario.id_usuario'))
)


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    email = db.Column(EmailType, unique=True)
    senha = db.Column(PasswordType(
            schemes=['pbkdf2_sha512']
        )
    )

    personagens = db.relationship('Personagem', back_populates="usuario")

    def __init__(self, nome=None, email=None, senha=None):
        self.nome = nome
        self.email = email
        self.senha = senha


class Campanha(db.Model):
    __tablename__ = 'campanha'
    id_campanha = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    mesas = db.relationship('Mesa', back_populates='campanha')

    mestres = db.relationship(
        'Usuario',
        secondary=campanha_mestres,
        backref=db.backref('campanhas_mestradas', lazy='dynamic')
    )

    jogadores = db.relationship(
        'Usuario',
        secondary=campanha_jogadores,
        backref=db.backref('campanhas_participando', lazy='dynamic')
    )

    def __init__(self, nome=None):
        self.nome = nome

    def papel(self, usuario):
        if usuario in self.mestres:
            return 'Mestre'
        elif usuario in self.jogadores:
            return 'Jogador'
        else:
            return '-'

    def is_mestre(self, usuario):
        if usuario in self.mestres:
            return True
        return False

    def is_jogador(self, usuario):
        if usuario in self.jogadores:
            return True
        return False


class Mesa(db.Model):
    __tablename__ = 'mesa'
    id_mesa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    personagens = db.relationship('Personagem', back_populates="mesa")

    campanha = db.relationship('Campanha', back_populates="mesas")
    id_campanha = db.Column(db.Integer, db.ForeignKey('campanha.id_campanha'))

    def __init__(self, nome=None):
        self.nome = nome


class Raca(db.Model):
    __tablename__ = 'raca'
    id_raca = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    def __init__(self, nome=None):
        self.nome = nome


class Classe(db.Model):
    __tablename__ = 'classe'
    id_classe = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_identity': __tablename__,
                       'polymorphic_on': tipo}

    def __init__(self, nome=None):
        self.nome = nome


class ClassePrestigio(Classe):
    __tablename__ = 'classe_prestigio'
    id_classe = db.Column(db.Integer(), db.ForeignKey("classe.id_classe", ondelete="CASCADE"), primary_key=True)
    nivel_max = db.Column(db.Integer)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome=None, nivel_max=None):
        Classe.__init__(self, nome)
        self.nivel_max = nivel_max


class InstanciaClasse(db.Model):
    __tablename__ = 'instancia_classe'
    id_instancia_classe = db.Column(db.Integer, primary_key=True)
    nivel = db.Column(db.Integer)

    id_classe = db.Column(db.Integer, db.ForeignKey('classe.id_classe'))
    classe = db.relationship('Classe', uselist=False)

    id_personagem = db.Column(db.Integer, db.ForeignKey('personagem.id_personagem'))

    def __init__(self, classe=None, nivel=None):
        self.classe = classe
        self.nivel = nivel

    def __str__(self):
        return self.classe.nome

class Personagem(db.Model):
    __tablename__ = 'personagem'
    id_personagem = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(200))
    exp = db.Column(db.Integer)

    raca = db.relationship('Raca')
    id_raca = db.Column(db.Integer, db.ForeignKey('raca.id_raca'))

    classes = db.relationship('InstanciaClasse')

    usuario = db.relationship('Usuario', back_populates="personagens")
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))

    mesa = db.relationship('Mesa', back_populates="personagens")
    id_mesa = db.Column(db.Integer, db.ForeignKey('mesa.id_mesa'))

    def __init__(self, nome=None, descricao=None):
        self.nome = nome
        self.descricao = descricao

    def str_classes(self):
        str = ''
        for x in range (len(self.classes)):
            str += self.classes[x].classe.nome
            if x != (len(self.classes)-1):
                str += ', '
        return str