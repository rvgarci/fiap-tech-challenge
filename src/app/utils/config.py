import os

from dotenv import load_dotenv

load_dotenv()

# Detecta ambiente
ENV = os.getenv("ENV", "local")
ENV = "development" if ENV == "local" else ENV

# Configura URI do banco com base no ambiente
if ENV == "production":
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
else:
    SQLALCHEMY_DATABASE_URI = "sqlite:///src/app/database/embrapa.db"

# Chaves de segurança
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_jwt_secret")

# SQLAlchemy config
SQLALCHEMY_TRACK_MODIFICATIONS = False
