from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.routers.routers import router

# from app.utils.database_helper import Base, engine

app = FastAPI(
    title="FIAP Tech Challenge - Embrapa API",
    description="API RESTful para acessar dados da Embrapa",
    version="0.1.0",
)

app.include_router(router)

# Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="src/app/templates")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
