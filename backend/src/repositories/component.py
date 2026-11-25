from src.models.component import ComponentOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import  ComponentDataMapper


class ComponentRepository(BaseRepository):
    model = ComponentOrm
    mapper = ComponentDataMapper