import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #Secret key configuration
    SECRET_KEY = 'This is a secret key'

    #RECAPTCHA_PUBLIC_KEY
    RECAPTCHA_PUBLIC_KEY = '6LehzKkUAAAAAOoocNyX38wX1rl6JfkgSgPtqcOD'

    #Database configuration
    # SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlist:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'sqlist:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False