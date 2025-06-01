from fastapi import APIRouter
from services import scraper
from models import model


router = APIRouter(prefix="/embrapa", tags=["Embrapa"])

"""@router.get("/producao", response_model=ProducaoModel)
def get_producao():
    return scrape_producao()"""


@router.get("/producao")
def get_producao():
    return {"message": ("Embrapa endpoint: PRODUÇÃO <RESULTADO DO SCRAPER>")}


@router.get("/processamento")
def get_processamento():
    return {"message": ("Embrapa endpoint: PROCESSAMENTO <RESULTADO DO SCRAPER>")}


@router.get("/comercializacao")
def get_comercializacao():
    return {"message": ("Embrapa endpoint: COMERCIALIZAÇÃO <RESULTADO DO SCRAPER>")}


@router.get("/importacao")
def get_importacao():
    return {"message": ("Embrapa endpoint: IMPORTAÇÃO <RESULTADO DO SCRAPER>")}


@router.get("/exportacao")
def get_exportacao():
    return {"message": ("Embrapa endpoint: EXPORTAÇÃO <RESULTADO DO SCRAPER>")}
