from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.scraper import (
    get_production_data,
    get_processing_data,
    get_commercial_data,
    get_import_data,
    get_export_data,
)
from app.services.db_writer import store_data
from app.models.models import (
    ProductionItemModel,
    ProcessingItemModel,
    CommercialItemModel,
    ImportItemModel,
    ExportItemModel,
)
from app.database import get_db

router = APIRouter(prefix="/admin", tags=["Administrador"])

@router.post("/load_all")
def load_all_data(db: Session = Depends(get_db)):
    anos = [2021, 2022, 2023]

    # Produção
    for ano in anos:
        store_data(get_production_data("producao", None, ano), ProductionItemModel, db)

    # Processamento: subcategorias
    suboptions_proc = ["viniferas", "americanas_e_hibridas", "uvas_de_mesa", "sem_classificacao"]
    for ano in anos:
        for sub in suboptions_proc:
            store_data(get_processing_data("processamento", sub, ano), ProcessingItemModel, db)

    # Comercialização
    for ano in anos:
        store_data(get_commercial_data("comercializacao", None, ano), CommercialItemModel, db)

    # Importação
    suboptions_imp = ["vinhos_de_mesa", "espumantes", "uvas_frescas", "uvas_passas", "sucos_de_uva"]
    for ano in anos:
        for sub in suboptions_imp:
            store_data(get_import_data("importacao", sub, ano), ImportItemModel, db)

    # Exportação
    suboptions_exp = ["vinhos_de_mesa", "espumantes", "uvas_frescas", "sucos_de_uva"]
    for ano in anos:
        for sub in suboptions_exp:
            store_data(get_export_data("exportacao", sub, ano), ExportItemModel, db)

    return {"status": f"Dados dos anos {anos} carregados com sucesso"}
