import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

# acá conectamos:  SQLAlchemy-PostgreSQL
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)