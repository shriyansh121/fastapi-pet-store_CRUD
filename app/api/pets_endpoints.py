from app.core.logging import setup_logger
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.core.database_connection.database_connection import get_db
from app.schemas.pet_pydantic import PetCreate, PetUpdate, PetInDB
from app.crud import crud_pet

logger = setup_logger()

router = APIRouter()

@router.post(
    "/",
    response_model=PetInDB,
    status_code=status.HTTP_201_CREATED
)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    logger.info("POST /pets | Create pet request received")

    db_pet = crud_pet.create_pet(db=db, pet=pet)

    logger.info(f"POST /pets | Pet created successfully id={db_pet.id}")
    return db_pet


@router.get("/", response_model=List[PetInDB])
def read_pets(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    logger.info(f"GET /pets | Fetch pets list (skip={skip}, limit={limit})")

    pets = crud_pet.get_pets(db, skip=skip, limit=limit)

    logger.info(f"GET /pets | Returned {len(pets)} pets")
    return pets


@router.get("/{pet_id}", response_model=PetInDB)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    logger.info(f"GET /pets/{pet_id} | Fetch pet")

    db_pet = crud_pet.get_pet(db, pet_id=pet_id)

    if db_pet is None:
        logger.warning(f"GET /pets/{pet_id} | Pet not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pet not found"
        )

    logger.info(f"GET /pets/{pet_id} | Pet found")
    return db_pet


@router.put("/{pet_id}", response_model=PetInDB)
def update_pet(
    pet_id: int,
    pet_update: PetUpdate,
    db: Session = Depends(get_db)
):
    logger.info(f"PUT /pets/{pet_id} | Update request received")

    db_pet = crud_pet.update_pet(
        db, pet_id=pet_id, pet_update=pet_update
    )

    if db_pet is None:
        logger.warning(f"PUT /pets/{pet_id} | Pet not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pet not found"
        )

    logger.info(f"PUT /pets/{pet_id} | Pet updated successfully")
    return db_pet


@router.delete(
    "/{pet_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    logger.info(f"DELETE /pets/{pet_id} | Delete request received")

    success = crud_pet.delete_pet(db, pet_id=pet_id)

    if not success:
        logger.warning(f"DELETE /pets/{pet_id} | Pet not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pet not found"
        )

    logger.info(f"DELETE /pets/{pet_id} | Pet deleted successfully")
    return None
