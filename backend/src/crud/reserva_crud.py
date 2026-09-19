from sqlmodel import Session, select

from models.auto_model import Auto
from models.reserva_model import Reserva

from schemas.reserva_schema import (
    ReservaCreate,
    ReservaUpdate
)


def crear_reserva(
    reserva: ReservaCreate,
    session: Session
):
    auto = session.get(
        Auto,
        reserva.auto_id
    )

    if not auto:
        return None

    nueva_reserva = Reserva.model_validate(
        reserva
    )

    session.add(nueva_reserva)
    session.commit()
    session.refresh(nueva_reserva)

    return nueva_reserva


def obtener_reservas(
    session: Session
):
    statement = select(Reserva)

    reservas = session.exec(
        statement
    ).all()

    return reservas


def obtener_reserva_por_id(
    reserva_id: int,
    session: Session
):
    return session.get(
        Reserva,
        reserva_id
    )


def actualizar_reserva(
    reserva_id: int,
    datos: ReservaUpdate,
    session: Session
):
    reserva = session.get(
        Reserva,
        reserva_id
    )

    if not reserva:
        return None

    if datos.auto_id is not None:
        auto = session.get(
            Auto,
            datos.auto_id
        )

        if not auto:
            return None

    nuevos_datos = datos.model_dump(
        exclude_unset=True
    )

    reserva.sqlmodel_update(
        nuevos_datos
    )

    session.add(reserva)
    session.commit()
    session.refresh(reserva)

    return reserva


def eliminar_reserva(
    reserva_id: int,
    session: Session
):
    reserva = session.get(
        Reserva,
        reserva_id
    )

    if not reserva:
        return None

    session.delete(reserva)
    session.commit()

    return reserva