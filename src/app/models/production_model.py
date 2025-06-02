# Importando as bibliotecas necessárias
from pydantic import BaseModel


class Production(BaseModel):
    tipo: str  # product type (e.g., "vinho", "suco")
    produto: str  # product name (e.g., "tinto", "branco")
    quantidade: int  # production quantity in liters [L]
    # Filter
        # ano: int
