# src/app/routers/routers.py

import logging

from fastapi import APIRouter

from app.routers.admin_router import router as admin_router
from app.routers.comercial_router import (
    router as comercial_router,  # ou commercial_router, se preferir
)
from app.routers.export_router import router as export_router
from app.routers.import_router import router as import_router
from app.routers.processing_router import router as processing_router
from app.routers.production_router import router as production_router

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/embrapa")

router.include_router(production_router, tags=["Produção"])
router.include_router(processing_router, tags=["Processamento"])
router.include_router(comercial_router, tags=["Comercialização"])
router.include_router(import_router, tags=["Importação"])
router.include_router(export_router, tags=["Exportação"])
router.include_router(admin_router, tags=["Admin"])

for r in router.routes:
    logger.info(f"✅ Rota incluída: {r.path}")
