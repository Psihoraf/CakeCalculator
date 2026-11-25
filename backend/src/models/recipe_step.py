from typing import TYPE_CHECKING

from sqlalchemy import Integer, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
if TYPE_CHECKING:
    from src.models.component import ComponentOrm

class RecipeStepOrm(Base):
    __tablename__ = "recipe_steps"

    __table_args__ = (
        UniqueConstraint(
            "component_id",
            "number",
            name="uq_component_step_number"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    component_id: Mapped[int] = mapped_column(
        ForeignKey("components.id", ondelete="CASCADE"),
        nullable=False
    )

    component: Mapped["ComponentOrm"] = relationship(
        "ComponentOrm",
        back_populates="steps"
    )