
from pydantic import BaseModel, ConfigDict, Field

from src.schemas.ingredient import (
    IngredientRequest,
    IngredientResponse,
    IngredientDB
)

from src.schemas.recipe_step import (
    RecipeStepRequest,
    RecipeStepResponse,
    RecipeStepDB
)


class ComponentRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)

    ingredients: list[IngredientRequest] = Field(
        min_length=1
    )

    steps: list[RecipeStepRequest] = Field(
        min_length=1
    )


class ComponentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    ingredients: list[IngredientResponse]
    steps: list[RecipeStepResponse]


class ComponentDB(BaseModel):
    name: str
    ingredients: list[IngredientDB]
    steps: list[RecipeStepDB]
