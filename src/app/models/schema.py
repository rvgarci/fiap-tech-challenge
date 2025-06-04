from pydantic import BaseModel
from typing import Optional


class ProductionItem(BaseModel):
    categoria: str
    produto: str
    quantidade_litros: int

class ProcessingItem(BaseModel):
    grupo: str
    cultivar: str
    quantidade_quilo: int


class CommercialItem(BaseModel):
    categoria: str
    produto: str
    quantidade_litros: int

class ImportItem(BaseModel):
    pais: str
    quantidade_quilo: Optional[int]
    valor_usd: Optional[float] 

class ExportItem(BaseModel):
    pais: str
    quantidade_quilo: Optional[int]
    valor_usd: Optional[float]
