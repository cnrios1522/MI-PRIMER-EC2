from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlmodel import Session

from database.database import get_session

from schemas.auto_schema import (
    AutoCreate,
    AutoUpdate,
    AutoPublic
)

from crud.auto_crud import (
    crear_auto,
    obtener_autos,
    obtener_auto_por_id,
    actualizar_auto,
    eliminar_auto
)


router = APIRouter(
    prefix="/autos",
    tags=["Autos"]
)


@router.post(
    "/",
    response_model=AutoPublic,
    status_code=status.HTTP_201_CREATED
)
def post_auto(
    auto: AutoCreate,
    session: Session = Depends(get_session)
):
    return crear_auto(
        auto,
        session
    )


@router.get(
    "/",
    response_model=list[AutoPublic]
)
def get_autos(
    session: Session = Depends(get_session)
):
    return obtener_autos(
        session
    )


@router.get(
    "/{auto_id}",
    response_model=AutoPublic
)
def get_auto(
    auto_id: int,
    session: Session = Depends(get_session)
):
    auto = obtener_auto_por_id(
        auto_id,
        session
    )

    if not auto:
        raise HTTPException(
            status_code=404,
            detail="Auto no encontrado"
        )

    return auto


@router.patch(
    "/{auto_id}",
    response_model=AutoPublic
)
def patch_auto(
    auto_id: int,
    datos: AutoUpdate,
    session: Session = Depends(get_session)
):
    auto = actualizar_auto(
        auto_id,
        datos,
        session
    )

    if not auto:
        raise HTTPException(
            status_code=404,
            detail="Auto no encontrado"
        )

    return auto


@router.delete(
    "/{auto_id}"
)
def delete_auto(
    auto_id: int,
    session: Session = Depends(get_session)
):
    auto = eliminar_auto(
        auto_id,
        session
    )

    if not auto:
        raise HTTPException(
            status_code=404,
            detail="Auto no encontrado"
        )

    return {
        "mensaje": "Auto eliminado correctamente"
    }