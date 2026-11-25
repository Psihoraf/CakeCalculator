from src.models.ingredient import IngredientOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import IngredientDataMapper


class IngredientRepository(BaseRepository):
    model = IngredientOrm
    mapper = IngredientDataMapper