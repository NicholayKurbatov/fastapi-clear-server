from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship

from server.db.pg_db import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    info = Column(String, nullable=False)
    data = Column(JSON, nullable=False)