from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import PG_USER, PG_PSWD, PG_HOST, PG_DB, PG_SSL

# connection config to posgresql
SQLALCHEMY_DATABASE_URL = f"postgresql+asincpg://{PG_USER}:{PG_PSWD}@%{PG_HOST}/{PG_DB}?sslmode=require"

# create SQLAlchemy "engine"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# create instance of the SessionLocal class will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base model class
Base = declarative_base()