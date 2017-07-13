from flask import Blueprint, render_template

mod_jogador = Blueprint('jogador', __name__, url_prefix='/jogador')

@mod_jogador.route('/')
def index():
    return render_template('jogador/index.html')