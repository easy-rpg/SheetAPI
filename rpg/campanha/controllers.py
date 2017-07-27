from flask import Blueprint, render_template

mod_mestre = Blueprint('mestre', __name__, url_prefix='/mestre')

@mod_mestre.route('/')
def index():
    return render_template('mestre/index.html')