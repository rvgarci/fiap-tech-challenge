import os
from dotenv import load_dotenv

load_dotenv()

# Configurações Sensíveis
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_jwt_secret")

# Configuração do banco SQLite
SQLALCHEMY_DATABASE_URI = "sqlite:///src/app/database/embrapa.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
