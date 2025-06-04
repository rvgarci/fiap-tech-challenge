from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.utils.config import SQLALCHEMY_DATABASE_URI

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind=engine, autocommit=False, autoflush=False
)

Base = declarative_base()
