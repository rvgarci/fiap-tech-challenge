# Estrutura de projeto FastAPI para o Tech Challenge
# Diretório: fiap_tech_challenge/app

# main.py
from fastapi import FastAPI
from app.routers import producao

app = FastAPI(title="API Embrapa - Tech Challenge")

# Include routers
app.include_router(producao.router)


@app.get("/")
def read_root():
    return {"message": "API Embrapa funcionando!"}


# routers/producao.py
from fastapi import APIRouter
from app.services.scraper_producao import coletar_dados_producao

router = APIRouter(prefix="/producao", tags=["Produção"])


@router.get("/")
def get_producao():
    dados = coletar_dados_producao()
    return dados


# services/scraper_producao.py
import requests
from bs4 import BeautifulSoup


def coletar_dados_producao():
    url = "https://www.embrapa.br/some/producao"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # Aqui você deve adaptar para extrair os dados reais
    return {"dados": "Fake - substituir pelo scraping real"}


# models/schemas.py
from pydantic import BaseModel


class ProducaoOut(BaseModel):
    titulo: str
    valor: str


# config.py
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")


# __init__.py
# (vazio por enquanto, apenas para tornar a pasta um pacote Python)


# requirements.txt (se não usar poetry)
fastapi
uvicorn
beautifulsoup4
requests
python - dotenv
