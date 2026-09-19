from sqlmodel import SQLModel


class AutoBase(SQLModel):
    marca: str
    modelo: str
    anio: int
    placa: str
    disponible: bool = True


class AutoCreate(AutoBase):
    pass


class AutoUpdate(SQLModel):
    marca: str | None = None
    modelo: str | None = None
    anio: int | None = None
    placa: str | None = None
    disponible: bool | None = None


class AutoPublic(AutoBase):
    id: int