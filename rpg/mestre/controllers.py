from flask import Blueprint, request

mod_mestre = Blueprint('mestre', __name__, url_prefix='/mestre', template_folder='templates')

@mod_mestre.route('/')
def index():
    return 'index mestre'