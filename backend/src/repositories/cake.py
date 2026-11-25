from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import CakeDataMapper
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.models.cake import CakeOrm
from src.models.component import ComponentOrm


class CakeRepository(BaseRepository):
    model = CakeOrm
    mapper = CakeDataMapper

    async def get_all(self):
        query = (
            select(self.model)
            .options(
                selectinload(CakeOrm.components)
                .selectinload(ComponentOrm.ingredients),

                selectinload(CakeOrm.components)
                .selectinload(ComponentOrm.steps)
            )
        )

        result = await self.session.execute(query)
        items = result.scalars().all()

        return [
            self.mapper.map_to_domain_entity(item)
            for item in items
        ]