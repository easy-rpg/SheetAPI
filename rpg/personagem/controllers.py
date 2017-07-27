from flask import Blueprint, render_template, redirect, g
from rpg.core.models import Personagem

mod_personagem = Blueprint('personagem', __name__, url_prefix='/personagem')


@mod_personagem.route('/')
def index():
    if g.usuario is None:
        return redirect('/login')

    return render_template('/personagem/index.html', usuario=g.usuario)


@mod_personagem.route('/<id_personagem>')
def ver_personagem(id_personagem):
    if g.usuario is None:
        return redirect('/login')

    personagem = Personagem.query.filter_by(id_personagem=id_personagem).first()
    return render_template('/personagem/ver.html', personagem=personagem, usuario=g.usuario)