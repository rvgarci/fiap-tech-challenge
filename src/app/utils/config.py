"""
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env, se houver

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dados.db")
JWT_SECRET = os.getenv("JWT_SECRET", "supersecret")

"""

