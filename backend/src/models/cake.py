from typing import TYPE_CHECKING

from sqlalchemy import String, Text, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.models.component import ComponentOrm

class CakeOrm(Base):
    __tablename__ = "cakes"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    base_diameter: Mapped[float] = mapped_column(
        Numeric(5, 2),
        nullable=False
    )

    image: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    components: Mapped[list["ComponentOrm"]] = relationship(
        "ComponentOrm",
        back_populates="cake",
        cascade="all, delete-orphan"
    )