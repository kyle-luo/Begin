import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_wtf import CsrfProtect

import sqlalchemy.dialects.sqlite

from config import Config

#init app with Flask
app = Flask(__name__, template_folder='../templates')

#flask-bootstrap render
bs = Bootstrap(app)

#csrfprotect config
CsrfProtect().init_app(app)

#implement config settings
app.config.from_object(Config)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

#implement database setting
db = SQLAlchemy(app)

#Bcrypt setting for encryption (like for password, etc)
bcrypt = Bcrypt(app)

from app.routes import *