from sqlmodel import Field

from schemas.reserva_schema import ReservaBase


class Reserva(ReservaBase, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True
    )

    auto_id: int = Field(
        foreign_key="auto.id"
    )