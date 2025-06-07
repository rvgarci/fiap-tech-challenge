from fastapi import APIRouter

from app.routers.admin_router import router as admin_router
from app.routers.comercial_router import router as comercial_router
from app.routers.export_router import router as export_router
from app.routers.import_router import router as import_router
from app.routers.processing_router import router as processing_router
from app.routers.production_router import router as production_router

router = APIRouter(prefix="/embrapa")

router.include_router(production_router)
router.include_router(processing_router)
router.include_router(comercial_router)
router.include_router(import_router)
router.include_router(export_router)
router.include_router(admin_router)

for r in router.routes:
    print(f"Rota incluída: {r.path}")
