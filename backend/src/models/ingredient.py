from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


if TYPE_CHECKING:
    from src.models.component import ComponentOrm

class IngredientOrm(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    amount: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    unit: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    component_id: Mapped[int] = mapped_column(
        ForeignKey("components.id", ondelete="CASCADE"),
        nullable=False
    )

    component: Mapped["ComponentOrm"] = relationship(
        "ComponentOrm",
        back_populates="ingredients"
    )