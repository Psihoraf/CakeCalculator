
from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from src.schemas.component import (
    ComponentRequest,
    ComponentResponse,
    ComponentDB
)


class CakeRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)

    description: str = Field(
        min_length=1,
        max_length=1000
    )

    base_diameter: float = Field(
        gt=0,
        le=100
    )

    image: HttpUrl | None = None

    components: list[ComponentRequest] = Field(
        min_length=1
    )


class CakeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str
    base_diameter: float
    image: str | None = None

    components: list[ComponentResponse]


class CakeDB(BaseModel):
    name: str
    description: str
    base_diameter: float
    image: str | None = None

    components: list[ComponentDB]
