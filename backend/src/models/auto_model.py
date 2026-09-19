from sqlmodel import Field

from schemas.auto_schema import AutoBase


class Auto(AutoBase, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True
    )