import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLE = True
    CSRF_SESSION_KEY = '86fcff6e4d4cc352dd68f357305e0b3b3571e2fbf76f64c443bc33287dd9e3a2'
    SECRET_KEY = 'cab53e6184a46681e28e46ad206acab8ff72677696d0dea71643af030a859bab'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ...


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR, 'app.db')
