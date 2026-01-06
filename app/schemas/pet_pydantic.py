from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal
from datetime import datetime

class PetBase(BaseModel):
    name: str
    species: str
    age: Optional[int] = None
    price: Optional[Decimal] = None
    is_available: bool = True

class PetCreate(PetBase):
    pass

class PetUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    age: Optional[int] = None
    price: Optional[Decimal] = None
    is_available: Optional[bool] = None

class PetInDB(PetBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)