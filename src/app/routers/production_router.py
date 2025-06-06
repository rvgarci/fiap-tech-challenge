from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.models.models import ProductionItemModel
from app.models.schema import ProductionItem
from app.services.db_writer import store_data
from app.services.scraper import get_production_data
from app.utils.database_helper import get_db


option = "producao"
router = APIRouter(prefix=f"/{option}", tags=["Produção"])

@router.get("", response_model=List[ProductionItem])
def production_route(year: int = Query(..., ge=1970, le=2023)):
    """
    Faz scraping da aba Produção e salva os dados no banco.
    """
    result = get_production_data(option, None, year)
    store_data(result, ProductionItemModel)
    return result

@router.get("/historico", response_model=List[ProductionItem])
def list_historico(db: Session = Depends(get_db)):
    """
    Retorna todos os dados de produção salvos no banco.
    """
    return db.query(ProductionItemModel).filter(ProductionItemModel.ano > 0).limit(100).all()

