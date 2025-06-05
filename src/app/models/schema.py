from pydantic import BaseModel
from typing import Optional


class ProductionItem(BaseModel):
    categoria: str
    produto: str
    quantidade_litros: int
    ano: int

    model_config = {"from_attributes": True}

class ProcessingItem(BaseModel):
    grupo: str
    cultivar: str
    quantidade_quilo: int
    ano: int

    model_config = {"from_attributes": True}

class CommercialItem(BaseModel):
    categoria: str
    produto: str
    quantidade_litros: int
    ano: int
    
    model_config = {"from_attributes": True}

class ImportItem(BaseModel):
    pais: str
    quantidade_quilo: Optional[int]
    valor_usd: Optional[float]
    ano: int

    model_config = {"from_attributes": True}

class ExportItem(BaseModel):
    pais: str
    quantidade_quilo: Optional[int]
    valor_usd: Optional[float]
    ano: int
    
    model_config = {"from_attributes": True}
