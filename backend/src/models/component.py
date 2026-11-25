from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base



if TYPE_CHECKING:
    from src.models.recipe_step import RecipeStepOrm
    from src.models.ingredient import IngredientOrm
    from src.models.cake import CakeOrm

class ComponentOrm(Base):
    __tablename__ = "components"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    cake_id: Mapped[int] = mapped_column(
        ForeignKey("cakes.id", ondelete="CASCADE"),
        nullable=False
    )

    cake: Mapped["CakeOrm"] = relationship(
        back_populates="components"
    )

    ingredients: Mapped[list["IngredientOrm"]] = relationship(
        back_populates="component",
        cascade="all, delete-orphan"
    )

    steps: Mapped[list["RecipeStepOrm"]] = relationship(
        "RecipeStepOrm",
        back_populates="component",
        cascade="all, delete-orphan",
        order_by="RecipeStepOrm.number"
    )