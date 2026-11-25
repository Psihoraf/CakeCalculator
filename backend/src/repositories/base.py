from sqlalchemy import select

from src.repositories.mappers.base import DataMapper


class BaseRepository:
    model = None
    mapper: DataMapper = None

    def __init__(self, session):
        self.session = session

    async def get_all(self):
        query = select(self.model)
        result = await self.session.execute(query)

        items = result.scalars().all()

        return [self.mapper.map_to_domain_entity(item) for item in items]

