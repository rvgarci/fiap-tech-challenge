from sqlalchemy import Column, Integer, String, Float
from app.utils.database_helper import Base


class ProductionItemModel(Base):
    __tablename__ = "production_items"
    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String, nullable=False)
    produto = Column(String, nullable=False)
    quantidade_litros = Column(Integer, nullable=False)

class ProcessingItemModel(Base):
    __tablename__ = "processing_items"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False) 
    grupo = Column(String, nullable=False)
    cultivar = Column(String, nullable=False)
    quantidade_quilo = Column(Integer, nullable=False)

class CommercialItemModel(Base):
    __tablename__ = "commercial_items"
    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String, nullable=False)
    produto = Column(String, nullable=False)
    quantidade_litros = Column(Integer, nullable=False)

class ImportItemModel(Base):
    __tablename__ = "import_items"
    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String, nullable=False)    
    pais = Column(String, nullable=False)
    quantidade_quilo = Column(Integer, nullable=True)
    valor_usd = Column(Float, nullable=True)

class ExportItemModel(Base):
    __tablename__ = "export_items"
    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String, nullable=False)    
    pais = Column(String, nullable=False)
    quantidade_quilo = Column(Integer, nullable=True)
    valor_usd = Column(Float, nullable=True)
