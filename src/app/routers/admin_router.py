from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.models import (
    CommercialItemModel,
    ExportItemModel,
    ImportItemModel,
    ProcessingItemModel,
    ProductionItemModel,
)
from app.services.db_writer import store_data
from app.services.scraper import (
    get_commercial_data,
    get_export_data,
    get_import_data,
    get_processing_data,
    get_production_data,
)
from app.utils.database_helper import get_db

router = APIRouter(prefix="/admin", tags=["Administrador"], include_in_schema=False)


@router.post("/load_all")
def load_all_data(db: Session = Depends(get_db)):
    anos = [2021, 2022, 2023]

    # Produção
    for ano in anos:
        store_data(get_production_data("producao", None, ano), ProductionItemModel)

    # Processamento: subcategorias
    suboptions_proc = [
        "viniferas",
        "americanas_e_hibridas",
        "uvas_de_mesa",
        "sem_classificacao",
    ]
    for ano in anos:
        for sub in suboptions_proc:
            store_data(
                get_processing_data("processamento", sub, ano), ProcessingItemModel, sub
            )

    # Comercialização
    for ano in anos:
        store_data(
            get_commercial_data("comercializacao", None, ano), CommercialItemModel
        )

    # Importação
    suboptions_imp = [
        "vinhos_de_mesa",
        "espumantes",
        "uvas_frescas",
        "uvas_passas",
        "sucos_de_uva",
    ]
    for ano in anos:
        for sub in suboptions_imp:
            store_data(get_import_data("importacao", sub, ano), ImportItemModel, sub)

    # Exportação
    suboptions_exp = ["vinhos_de_mesa", "espumantes", "uvas_frescas", "sucos_de_uva"]
    for ano in anos:
        for sub in suboptions_exp:
            store_data(get_export_data("exportacao", sub, ano), ExportItemModel, sub)

    return {"status": f"Dados dos anos {anos} carregados com sucesso"}
