import logging
from sqlalchemy.orm import Session
from app.models.pet_ORM import Pet
from app.schemas.pet_pydantic import PetBase, PetCreate, PetUpdate
from app.core.logging import setup_logger

logger = setup_logger()

def get_pet(db: Session, pet_id: int):
    logger.info(f"Fetching pet with id={pet_id}")
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if pet:
        logger.info(f"Pet with id={pet_id} found")
    else:
        logger.info(f"Pet with id={pet_id} not found")
    return pet

def get_pets(db: Session, skip:int=0, limit:int=100):
    logger.info(f"Fetching pets list (skip={skip}, limit={limit})")
    pets = db.query(Pet).offset(skip).limit(limit).all()
    logger.info(f"Fetched {len(pets)} pets")
    return pets

def create_pet(db: Session, pet: PetCreate):
    logger.info(f"Creating pet with data={pet.model_dump()}") #Model dump extracts validated data from a Pydantic model so other systems (ORM, DB, JSON) can use it.
    try:
        db_pet = Pet(**pet.model_dump())
        db.add(db_pet)
        db.commit()
        db.refresh(db_pet)
        logger.info(f"Pet created successfully with id={db_pet.id}")
        return db_pet
    except Exception as e:
        db.rollback()
        logger.error("Error while creating pet", exc_info=True)
        raise e

def update_pet(db: Session, pet_id: int, pet_update: PetUpdate):
    logger.info(f"Updating pet with id={pet_id}")
    pet = get_pet(db, pet_id)
    if not pet:
        logger.warning(f"Update failed: Pet not found id={pet_id}")
        return None
    update_data = pet_update.model_dump(exclude_unset=True)

    if not update_data:
        logger.warning(f"No fields provided to update for pet id={pet_id}")
        return pet

    logger.info(f"Updating fields for pet id={pet_id}: {list(update_data.keys())}")
    try:
        for key, value in update_data.items():
            setattr(pet, key, value)
        db.add(pet)
        db.commit()
        db.refresh(pet)
        logger.info(f"Pet updated successfully with id={pet_id}")
        return pet
    except Exception as e:
        db.rollback()
        logger.error("Error while updating pet", exc_info=True)
        raise e

def delete_pet(db: Session, pet_id: int):
    logger.info(f"Deleting pet with id={pet_id}")
    pet = get_pet(db, pet_id)
    if not pet:
        logger.info(f"Pet with id={pet_id} not found")
        return False
    try:
        db.delete(pet)
        db.commit()
        logger.info(f"Pet deleted successfully with id={pet_id}")
        return True
    except Exception as e:
        db.rollback()
        logger.error("Error while deleting pet", exc_info=True)
        raise e