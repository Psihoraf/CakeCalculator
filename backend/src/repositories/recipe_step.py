from src.models.recipe_step import RecipeStepOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ComponentDataMapper


class RecipeStepRepository(BaseRepository):
    model = RecipeStepOrm
    mapper = ComponentDataMapper

