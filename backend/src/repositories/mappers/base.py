from typing import TypeVar

from pydantic import BaseModel

from src.database import Base


SchemaType = TypeVar("SchemaType", bound=BaseModel)
DBModelType = TypeVar("DBModelType", bound=Base)


class DataMapper:
    model: type[DBModelType] = None
    response_schema: type[SchemaType] = None


    @classmethod
    def map_to_domain_entity(cls, data):
        return cls.response_schema.model_validate(
            data,
            from_attributes=True
        )

    @classmethod
    def map_to_persistence_entity(cls, data):
        return cls.model(**data.model_dump())

    @classmethod
    def map_nested_to_persistence_entity(cls, data, mapper):
        return [mapper.map_to_domain_entity(item) for item in data]
