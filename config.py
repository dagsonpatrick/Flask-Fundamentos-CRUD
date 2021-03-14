DEBUG = True

USERNAME = 'root'
PASSWORD = 'Wam293031@'
SERVER = 'localhost'
DB = 'flask_fundamentos_crud'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "minha-chave-secreta"

BABEL_DEFAULT_LOCALE = 'pt'