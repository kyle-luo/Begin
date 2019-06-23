from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_wtf import CsrfProtect

from config import Config

#init app with Flask
app = Flask(__name__, template_folder='../templates')

#flask-bootstrap render
bs = Bootstrap(app)

#csrfprotect config
CsrfProtect().init_app(app)

#implement database setting
db = SQLAlchemy(app)

#Bcrypt setting for encryption (like for password, etc)
bcrypt = Bcrypt(app)

#implement config settings
app.config.from_object(Config)

from app.routes import *