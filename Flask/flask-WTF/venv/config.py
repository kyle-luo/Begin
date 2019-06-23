import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #Secret key configuration
    SECRET_KEY = 'This is a secret key'

    #RECAPTCHA_PUBLIC_KEY
    RECAPTCHA_PUBLIC_KEY = '6LehzKkUAAAAAOoocNyX38wX1rl6JfkgSgPtqcOD'

    #RECAPTCHA_PRIVATE_KEY
    RECAPTCHA_PRIVATE_KEY = '6LehzKkUAAAAABHWvHkpr-7VYG09ZT3pp6XPtKf0'

    #Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = 'sqlist:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #CSRF token never expire
    WTF_CSRF_TIME_LIMIT = None