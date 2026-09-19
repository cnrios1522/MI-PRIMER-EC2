from sqlmodel import Session, select

from models.auto_model import Auto
from schemas.auto_schema import (
    AutoCreate,
    AutoUpdate
)


def crear_auto(
    auto: AutoCreate,
    session: Session
):
    nuevo_auto = Auto.model_validate(auto)

    session.add(nuevo_auto)
    session.commit()
    session.refresh(nuevo_auto)

    return nuevo_auto


def obtener_autos(
    session: Session
):
    statement = select(Auto)

    autos = session.exec(
        statement
    ).all()

    return autos


def obtener_auto_por_id(
    auto_id: int,
    session: Session
):
    return session.get(
        Auto,
        auto_id
    )


def actualizar_auto(
    auto_id: int,
    datos: AutoUpdate,
    session: Session
):
    auto = session.get(
        Auto,
        auto_id
    )

    if not auto:
        return None

    nuevos_datos = datos.model_dump(
        exclude_unset=True
    )

    auto.sqlmodel_update(
        nuevos_datos
    )

    session.add(auto)
    session.commit()
    session.refresh(auto)

    return auto


def eliminar_auto(
    auto_id: int,
    session: Session
):
    auto = session.get(
        Auto,
        auto_id
    )

    if not auto:
        return None

    session.delete(auto)
    session.commit()

    return auto