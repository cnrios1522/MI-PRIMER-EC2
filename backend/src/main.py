from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.database import create_db_and_tables

from routers.auto_router import router as auto_router
from routers.reserva_router import router as reserva_router

# Importamos los modelos para registrar las tablas
from models.auto_model import Auto
from models.reserva_model import Reserva


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="API de Autos y Reservas",
    description="API REST CRUD para administrar autos y reservas",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(
    auto_router
)

app.include_router(
    reserva_router
)


@app.get(
    "/",
    tags=["Inicio"]
)
def inicio():
    return {
        "mensaje": "API de Nicolas Rios",
    }