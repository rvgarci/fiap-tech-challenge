from typing import Type
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from pydantic import BaseModel
from app.utils.database_helper import SessionLocal


def store_data(
    items: list[BaseModel], model: Type[DeclarativeMeta], suboption: str = None
):
    db: Session = SessionLocal()
    try:
        model_columns = {col.name for col in model.__table__.columns}
        for item in items:
            data = item.model_dump(mode="json")
            pydantic_fields = set(data.keys())
            extra_fields = model_columns - pydantic_fields - {"id"}
            for extra in extra_fields:
                if suboption is not None:
                    data[extra] = suboption
            filtered_data = {k: v for k, v in data.items() if k in model_columns}
            row = model(**filtered_data)
            db.add(row)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
    finally:
        db.close()
