from flask import Blueprint, request

mod_jogador = Blueprint('jogador', __name__, url_prefix='/jogador', template_folder='templates')

@mod_jogador.route('/')
def index():
    return 'index jogador'