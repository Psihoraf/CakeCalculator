from src.models.cake import CakeOrm
from src.models.component import ComponentOrm
from src.models.ingredient import IngredientOrm
from src.models.recipe_step import RecipeStepOrm

from src.repositories.mappers.base import DataMapper

from src.schemas.cake import CakeResponse
from src.schemas.component import ComponentResponse
from src.schemas.ingredient import IngredientResponse
from src.schemas.recipe_step import RecipeStepResponse


class CakeDataMapper(DataMapper):
    model = CakeOrm
    response_schema = CakeResponse



class IngredientDataMapper(DataMapper):
    model = IngredientOrm
    response_schema = IngredientResponse


class ComponentDataMapper(DataMapper):
    model = ComponentOrm
    response_schema = ComponentResponse


class RecipeStepDataMapper(DataMapper):
    model = RecipeStepOrm
    response_schema = RecipeStepResponse