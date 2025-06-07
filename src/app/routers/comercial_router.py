from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.models.models import CommercialItemModel
from app.models.schema import CommercialItem
from app.services.db_writer import store_data
from app.services.scraper import get_commercial_data
from app.utils.database_helper import get_db

option = "comercializacao"
router = APIRouter(prefix=f"/{option}", tags=["Comercialização"])


@router.get("", response_model=List[CommercialItem])
def commercial_route(year: int = Query(..., ge=1970, le=2023)):
    """
    Faz scraping da aba Comercialização e armazena os dados.
    """
    result = get_commercial_data(option, None, year)
    store_data(result, CommercialItemModel)
    return result


@router.get("/historico", response_model=List[CommercialItem])
def list_historico(db: Session = Depends(get_db)):
    """
    Retorna todos os dados de comercialização salvos no banco.
    """
    return (
        db.query(CommercialItemModel)
        .filter(CommercialItemModel.year > 0)
        .limit(100)
        .all()
    )
