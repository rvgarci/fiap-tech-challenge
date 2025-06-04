from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.models.models import ProcessingItemModel
from app.models.schema import ProcessingItem
from app.services.db_writer import store_data
from app.services.scraper import get_processing_data
from app.utils.database_helper import get_db


option = "processamento"
suboptions = [
    "viniferas",
    "americanas_e_hibridas",
    "uvas_de_mesa",
    "sem_classificacao"
]

router = APIRouter(prefix=f"/{option}", tags=["Processamento"])

def create_scraping_route(suboption: str):
    async def scraping_route(year: int = Query(..., ge=1970, le=2024)) -> List[ProcessingItem]:
        result = get_processing_data(option, suboption, year)
        store_data(result, ProcessingItemModel, suboption)
        return result
    return scraping_route

def create_historico_route(suboption: str):
    async def historico_route(db: Session = Depends(get_db)) -> List[ProcessingItem]:
        return db.query(ProcessingItemModel).all()
    return historico_route

for sub in suboptions:
    router.add_api_route(
        path=f"/{sub}",
        endpoint=create_scraping_route(sub),
        methods=["GET"],
        name=f"{sub}_scraping"
    )
    router.add_api_route(
        path=f"/{sub}/historico",
        endpoint=create_historico_route(sub),
        methods=["GET"],
        name=f"{sub}_historico"
    )
