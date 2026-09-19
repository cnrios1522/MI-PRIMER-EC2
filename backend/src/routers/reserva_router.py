from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlmodel import Session

from database.database import get_session

from schemas.reserva_schema import (
    ReservaCreate,
    ReservaUpdate,
    ReservaPublic
)

from crud.reserva_crud import (
    crear_reserva,
    obtener_reservas,
    obtener_reserva_por_id,
    actualizar_reserva,
    eliminar_reserva
)


router = APIRouter(
    prefix="/reservas",
    tags=["Reservas"]
)


@router.post(
    "/",
    response_model=ReservaPublic,
    status_code=status.HTTP_201_CREATED
)
def post_reserva(
    reserva: ReservaCreate,
    session: Session = Depends(get_session)
):
    nueva_reserva = crear_reserva(
        reserva,
        session
    )

    if not nueva_reserva:
        raise HTTPException(
            status_code=404,
            detail="El auto indicado no existe"
        )

    return nueva_reserva


@router.get(
    "/",
    response_model=list[ReservaPublic]
)
def get_reservas(
    session: Session = Depends(get_session)
):
    return obtener_reservas(
        session
    )


@router.get(
    "/{reserva_id}",
    response_model=ReservaPublic
)
def get_reserva(
    reserva_id: int,
    session: Session = Depends(get_session)
):
    reserva = obtener_reserva_por_id(
        reserva_id,
        session
    )

    if not reserva:
        raise HTTPException(
            status_code=404,
            detail="Reserva no encontrada"
        )

    return reserva


@router.patch(
    "/{reserva_id}",
    response_model=ReservaPublic
)
def patch_reserva(
    reserva_id: int,
    datos: ReservaUpdate,
    session: Session = Depends(get_session)
):
    reserva = actualizar_reserva(
        reserva_id,
        datos,
        session
    )

    if not reserva:
        raise HTTPException(
            status_code=404,
            detail="Reserva o auto no encontrado"
        )

    return reserva


@router.delete(
    "/{reserva_id}"
)
def delete_reserva(
    reserva_id: int,
    session: Session = Depends(get_session)
):
    reserva = eliminar_reserva(
        reserva_id,
        session
    )

    if not reserva:
        raise HTTPException(
            status_code=404,
            detail="Reserva no encontrada"
        )

    return {
        "mensaje": "Reserva eliminada correctamente"
    }