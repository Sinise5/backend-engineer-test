from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  # ✅ tambahkan ini

from app.core.config import settings

engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # ✅ tambahkan ini

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
