from sqlalchemy import Column, Float, Integer, String, UniqueConstraint

from app.utils.database_helper import Base


class BaseItemModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    quantity = Column(Float, nullable=True)
    unit_of_measure = Column(String, nullable=False)
    year = Column(Integer, nullable=False)


class ProductionItemModel(BaseItemModel):
    __tablename__ = "production_item"
    __mapper_args__ = {"polymorphic_identity": "production_item"}
    category = Column(String, nullable=False)
    product = Column(String, nullable=False)
    __table_args__ = (
        UniqueConstraint(
            "type",
            "product",
            "year",
            name="uq_production_item_type_product_year",
        ),
    )


class ProcessingItemModel(BaseItemModel):
    __tablename__ = "processing_item"
    __mapper_args__ = {"polymorphic_identity": "processing_item"}
    color = Column(String, nullable=False)
    cultivar = Column(String, nullable=False)
    __table_args__ = (
        UniqueConstraint("cultivar", "year", name="uq_processing_item_cultivar_year"),
    )


class CommercialItemModel(BaseItemModel):
    __tablename__ = "commercial_item"
    __mapper_args__ = {"polymorphic_identity": "commercial_item"}
    category = Column(String, nullable=False)
    product = Column(String, nullable=False)
    __table_args__ = (
        UniqueConstraint(
            "type",
            "product",
            "year",
            name="uq_commercial_item_type_product_year",
        ),
    )


class ImportItemModel(BaseItemModel):
    __tablename__ = "import_item"
    __mapper_args__ = {"polymorphic_identity": "import_item"}
    country = Column(String, nullable=False)
    value = Column(Float, nullable=True)
    currency = Column(String, nullable=False)
    __table_args__ = (
        UniqueConstraint(
            "type", "country", "year", name="uq_import_item_type_country_year"
        ),
    )


class ExportItemModel(BaseItemModel):
    __tablename__ = "export_item"
    __mapper_args__ = {"polymorphic_identity": "export_item"}
    country = Column(String, nullable=False)
    value = Column(Float, nullable=True)
    currency = Column(String, nullable=False)
    __table_args__ = (
        UniqueConstraint(
            "type", "country", "year", name="uq_export_item_type_country_year"
        ),
    )
