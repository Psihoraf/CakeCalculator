
from pydantic import BaseModel, ConfigDict, Field


class RecipeStepRequest(BaseModel):
    number: int = Field(ge=1)
    description: str = Field(min_length=1, max_length=2000)


class RecipeStepResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number: int
    description: str


class RecipeStepDB(BaseModel):
    number: int
    description: str
