from fastapi import APIRouter
from services.production_scraper import get_production_data

router = APIRouter(prefix="/embrapa")


@router.get("/producao", tags=["Produção"])
def production_route():
    response = get_production_data("producao", None, 1985)
    return response

@router.get("/processamento", tags=["Processamento"])
def processing_route():
    response = get_production_data("processamento", None, 1985)
    return response

@router.get("/comercializacao", tags=["Comercialização"])
def commercial_route():
    response = get_production_data("comercializacao", None, 1985)
    return response

@router.get("/importacao", tags=["Importação"])
def import_route():
    response = get_production_data("importacao", None, 1985)
    return response

@router.get("/exportacao", tags=["Exportação"])
def export_route():
    response = get_production_data("exportacao", None, 1985)
    return response
