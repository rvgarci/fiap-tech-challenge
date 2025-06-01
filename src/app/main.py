# Importando as bibliotecas necessárias
from fastapi import FastAPI
from routers import embrapa

# Inicializando a aplicação FastAPI
app = FastAPI(
    title="API Embrapa - Tech Challenge",
    version="1.0.0",
    description="Scraping de dados da Embrapa e base para uso futuro com ML",
)

# Importando os módulos de rotas
app.include_router(embrapa.router)


# Rota de exemplo para verificar se a API está funcionando
@app.get("/")
def home():
    return {"message": "API Embrapa funcionando!"}
