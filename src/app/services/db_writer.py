# from typing import Type

# from pydantic import BaseModel
# from sqlalchemy.ext.declarative import DeclarativeMeta
# from sqlalchemy.orm import Session

# from app.utils.database_helper import SessionLocal

# def store_data(
#     items: list[BaseModel], model: Type[DeclarativeMeta], suboption: str = None
# ):
#     db: Session = SessionLocal()
#     try:
#         model_columns = {col.name for col in model.__table__.columns}
#         for item in items:
#             data = item.model_dump(mode="json")
#             pydantic_fields = set(data.keys())
#             extra_fields = model_columns - pydantic_fields - {"id"}
#             for extra in extra_fields:
#                 if suboption is not None:
#                     data[extra] = suboption
#             filtered_data = {k: v for k, v in data.items() if k in model_columns}
#             row = model(**filtered_data)
#             db.add(row)
#         try:
#             db.commit()
#         except Exception as e:
#             db.rollback()
#             raise e
#     finally:
#         db.close()


from typing import List, Type

from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Session

from app.utils.database_helper import SessionLocal


def store_data(
    items: List[BaseModel],
    model: Type[DeclarativeMeta],
    suboption: str = None,
):
    db: Session = SessionLocal()
    try:
        model_columns = {col.name for col in model.__table__.columns}
        for item in items:
            data = item.model_dump(mode="json")

            if suboption and "suboption" in model_columns:
                data["suboption"] = suboption

            # 🔍 Define chaves únicas para cada modelo
            filters = []
            if model.__tablename__ == "production_item":
                filters = [
                    model.type == data["type"],
                    model.product == data["product"],
                    model.year == data["year"],
                ]
            elif model.__tablename__ == "processing_item":
                filters = [
                    model.cultivar == data["cultivar"],
                    model.year == data["year"],
                ]
            elif model.__tablename__ == "commercial_item":
                filters = [
                    model.type == data["type"],
                    model.product == data["product"],
                    model.year == data["year"],
                ]
            elif model.__tablename__ in ["import_item", "export_item"]:
                filters = [
                    model.type == data["type"],
                    model.country == data["country"],
                    model.year == data["year"],
                ]

            # 🔁 Verifica se já existe
            instance = db.query(model).filter(*filters).first() if filters else None

            if instance:
                for key, value in data.items():
                    if key in model_columns and key != "id":
                        setattr(instance, key, value)
            else:
                new_row = model(**{k: v for k, v in data.items() if k in model_columns})
                db.add(new_row)

        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"[ERRO] Conflito de integridade: {e}")
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
