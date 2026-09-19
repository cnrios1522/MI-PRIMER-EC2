from datetime import date

from sqlmodel import SQLModel


class ReservaBase(SQLModel):
    cliente: str
    fecha_inicio: date
    fecha_fin: date
    auto_id: int
    estado: str = "pendiente"


class ReservaCreate(ReservaBase):
    pass


class ReservaUpdate(SQLModel):
    cliente: str | None = None
    fecha_inicio: date | None = None
    fecha_fin: date | None = None
    auto_id: int | None = None
    estado: str | None = None


class ReservaPublic(ReservaBase):
    id: int