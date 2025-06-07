from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.models.models import ExportItemModel
from app.models.schema import ExportItem
from app.services.db_writer import store_data
from app.services.scraper import get_export_data
from app.utils.database_helper import get_db

option = "exportacao"
suboptions = ["vinhos_de_mesa", "espumantes", "uvas_frescas", "sucos_de_uva"]

router = APIRouter(prefix=f"/{option}", tags=["Exportação"])


def create_scraping_route(suboption: str):
    async def scraping_route(
        year: int = Query(..., ge=1970, le=2024)
    ) -> List[ExportItem]:
        result = get_export_data(option, suboption, year)
        store_data(result, ExportItemModel, suboption)
        return result

    return scraping_route


def create_historico_route(suboption: str):
    async def historico_route(db: Session = Depends(get_db)) -> List[ExportItem]:
        return (
            db.query(ExportItemModel).filter(ExportItemModel.year > 0).limit(100).all()
        )

    return historico_route


for sub in suboptions:
    router.add_api_route(
        path=f"/{sub}",
        endpoint=create_scraping_route(sub),
        methods=["GET"],
        name=f"{sub}_scraping",
    )
    router.add_api_route(
        path=f"/{sub}/historico",
        endpoint=create_historico_route(sub),
        methods=["GET"],
        name=f"{sub}_historico",
    )
