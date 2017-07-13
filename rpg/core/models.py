from rpg import db
from sqlalchemy_utils import EmailType, PasswordType


mestres = db.Table(
    'mestres',
    db.Column('id_campanha', db.Integer, db.ForeignKey('campanha.id_campanha')),
    db.Column('id_usuario', db.Integer, db.ForeignKey('usuario.id_usuario'))
)


jogadores = db.Table(
    'jogadores',
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

    personagens = db.relationship('Personagem')

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Campanha(db.Model):
    __tablename__ = 'campanha'
    id_campanha = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    personagens = db.relationship('Personagem')

    mestres = db.relationship(
        'Usuario',
        secondary=mestres,
        backref=db.backref('campanhas_mestradas', lazy='dynamic')
    )

    jogadores = db.relationship(
        'Usuario',
        secondary=jogadores,
        backref=db.backref('campanhas_participando', lazy='dynamic')
    )

    def __init__(self, nome):
        self.nome = nome


class Raca(db.Model):
    __tablename__ = 'raca'
    id_raca = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))


class Classe(db.Model):
    __tablename__ = 'classe'
    id_classe = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_identity': __tablename__,
                       'polymorphic_on': tipo}

    def __init__(self, nome):
        self.nome = nome


class ClassePrestigio(Classe):
    __tablename__ = 'classe_prestigio'
    id_classe = db.Column(db.Integer(), db.ForeignKey("classe.id_classe", ondelete="CASCADE"), primary_key=True)
    nivel_max = db.Column(db.Integer)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome, nivel_max):
        Classe.__init__(self, nome)
        self.nivel_max = nivel_max


class InstanciaClasse(db.Model):
    __tablename__ = 'instancia_classe'
    id_instancia_classe = db.Column(db.Integer, primary_key=True)
    nivel = db.Column(db.Integer)

    id_classe = db.Column(db.Integer, db.ForeignKey('classe.id_classe'))
    classe = db.relationship('Classe', uselist=False)

    id_personagem = db.Column(db.Integer, db.ForeignKey('personagem.id_personagem'))


class Personagem(db.Model):
    __tablename__ = 'personagem'
    id_personagem = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(200))
    exp = db.Column(db.Integer)

    classes = db.relationship('InstanciaClasse')
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_campanha = db.Column(db.Integer, db.ForeignKey('campanha.id_campanha'))
