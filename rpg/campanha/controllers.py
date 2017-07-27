from flask import Blueprint, render_template

mod_campanha = Blueprint('campanha', __name__, url_prefix='/campanha')

@mod_campanha.route('/')
def index():
    return render_template('campanha/index.html')