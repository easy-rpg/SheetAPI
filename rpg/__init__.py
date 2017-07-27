from flask import Flask, g, session
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import logging
from logging.handlers import RotatingFileHandler
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Add log handler
handler = RotatingFileHandler(app.config['LOGGING_LOCATION'], maxBytes=100000, backupCount=50)
formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


from rpg.core.models import *


@app.errorhandler(404)
def not_found(error):
    app.logger.error(error)
    return error


@app.errorhandler(403)
def not_authorized(error):
    app.logger.error(error)
    return error


@app.before_request
def load_current_user():
    if 'id_usuario' in session:
        g.usuario = Usuario.query.filter_by(id_usuario=session['id_usuario']).first()
    else:
        g.usuario = None


from rpg.core.controllers import mod_core as core_module
from rpg.campanha.controllers import mod_campanha as campanha_module
from rpg.personagem.controllers import mod_personagem as personagem_module

app.register_blueprint(core_module)
app.register_blueprint(campanha_module)
app.register_blueprint(personagem_module)

db.create_all()