from src.services.base import BaseService


class CakeService(BaseService):
    async def get_cakes(self):
        return await self.db.cakes.get_all()