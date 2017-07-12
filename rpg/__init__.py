from flask import Flask
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

@app.errorhandler(404)
def not_found(error):
    app.logger.error(error)
    return error

@app.errorhandler(403)
def not_authorized(error):
    app.logger.error(error)
    return error

from app.core import models

from app.gm.controllers import mod_gm as gm_module
from app.player.controllers import mod_player as player_module

app.register_blueprint(gm_module)
app.register_blueprint(player_module)

db.create_all()