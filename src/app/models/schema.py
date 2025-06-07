from typing import Optional

from pydantic import BaseModel


class BaseItem(BaseModel):
    type: str
    quantity: Optional[float]
    unit_of_measure: str
    year: int

    model_config = {"from_attributes": True}


class ProductionItem(BaseItem):
    category: str
    product: str


class ProcessingItem(BaseItem):
    color: str
    cultivar: str


class CommercialItem(ProductionItem):
    pass


class ImportItem(BaseItem):
    country: str
    value: Optional[float]
    currency: str


class ExportItem(ImportItem):
    pass
