
from pydantic import BaseModel, ConfigDict, Field


class IngredientRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)
    unit: str = Field(min_length=1, max_length=20)


class IngredientResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    amount: float
    unit: str


class IngredientDB(BaseModel):
    name: str
    amount: float
    unit: str
