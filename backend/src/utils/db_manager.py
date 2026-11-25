from src.repositories.cake import CakeRepository
from src.repositories.ingredient import IngredientRepository
from src.repositories.component import ComponentRepository
from src.repositories.recipe_step import RecipeStepRepository


class DBManager:

    def __init__(self, session_factory):
        self.session_factory =session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.cakes = CakeRepository(self.session)
        self.components = ComponentRepository(self.session)
        self.ingredients = IngredientRepository(self.session)
        self.recipe_steps = RecipeStepRepository(self.session)

        return self


    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()