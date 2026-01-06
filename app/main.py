from fastapi import FastAPI
from app.api.pets_endpoints import router
from app.core.database_connection.database_connection import engine, Base
from app.core import logging


# NOTE: In a real production app, you should use migrations (e.g., Alembic)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Pet Store Management API",
    description="A simple FastAPI CRUD application for managing a pet store.",
    version="1.0.0"
)

# Include routers
app.include_router(router, prefix="/api/v1/pets", tags=["pets"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pet Store Management API"}