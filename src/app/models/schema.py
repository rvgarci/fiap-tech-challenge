# Importando as bibliotecas necessárias
from pydantic import BaseModel


class ProducaoResponse(BaseModel):
    produto: str
    quantidade: int
