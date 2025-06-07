from fastapi import FastAPI

from app.routers.routers import router
from app.utils.database_helper import Base, engine

app = FastAPI(
    title="FIAP Tech Challenge - Embrapa API",
    description="API RESTful para acessar dados da Embrapa",
    version="0.1.0",
)

app.include_router(router)
Base.metadata.create_all(bind=engine)
