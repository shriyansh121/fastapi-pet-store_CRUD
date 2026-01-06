from sqlalchemy import Column, Integer, String , Numeric, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database_connection.database_connection import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    species = Column(String(50), nullable=False)
    age = Column(Integer, nullable=True)
    price = Column(Numeric(10, 2), nullable=True)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())