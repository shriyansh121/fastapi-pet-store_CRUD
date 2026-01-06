from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from app.core.logging import setup_logger
from dotenv import load_dotenv

load_dotenv()

logger = setup_logger()

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

logger.debug('Creating engine for the database')
engine = create_engine(DATABASE_URL, pool_pre_ping = True)

logger.debug("creating a session with the database.")
SessionLocal = sessionmaker(
    autocommit = False, 
    #Why this is good:
    #Prevents accidental writes
    # Allows rollback on error
    autoflush=False, # Sends changes to DB before every query and chnages stays in memory
    bind = engine # Session will use that engine to talk with the database
)
# Session = a conversation with the database
# You don’t talk to DB directly — you talk via a session.

Base = declarative_base() # Base = the parent class for all ORM models

def test_db_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Database connection established successfully")
    except Exception as e:
        logger.error("Database connection failed", exc_info=True)
        raise e

test_db_connection() # test the connection

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# The database connection infrastructure is already established, and sessions are separate 
# units of work created per request/user.