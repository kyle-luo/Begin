from flask import Flask

from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_wtf import CsrfProtect
from flask_login import LoginManager

from config import Config

#init app with Flask
app = Flask(__name__, template_folder='../templates')

#implement config settings
app.config.from_object(Config)

#flask-bootstrap render
bs = Bootstrap(app)

#csrfprotect config
CsrfProtect().init_app(app)

#Bcrypt setting for encryption (like for password, etc)
bcrypt = Bcrypt(app)

#Login settings
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'You must login to access this page'
login.login_message_category = 'info'

from app.routes import *
from app.init_db import *