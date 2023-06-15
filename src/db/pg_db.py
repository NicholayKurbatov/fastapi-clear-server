from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ssl import create_default_context, CERT_REQUIRED

from .config import PG_USER, PG_PSWD, PG_HOST, PG_DB, PG_SSL


# connection config to posgresql
SQLALCHEMY_DATABASE_URL = f"postgresql://{PG_USER}:{PG_PSWD}@{PG_HOST}/{PG_DB}"

# load ssl cert
ssl_context = create_default_context(cafile=PG_SSL)
ssl_context.verify_mode = CERT_REQUIRED

# create SQLAlchemy "engine"
engine = create_engine(
   SQLALCHEMY_DATABASE_URL,
   connect_args={"ssl": ssl_context},
   pool_pre_ping=True,
   future=True,
   echo=True,
)

# create instance of the SessionLocal class will be a database session
SessionLocal = sessionmaker(
    bind=engine, 
    autocommit=False, 
    autoflush=False, 
)

# base model class
Base = declarative_base()