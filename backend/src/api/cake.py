from fastapi import APIRouter

from src.services.cake import CakeService
from src.utils.db_manager import DBManager
from src.utils.dependencies import DBDep

router = APIRouter(prefix='/cake', tags=['Торты'])

@router.get("/{cake_id}")
async def get_cakes(db:DBDep):
    return await db.cakes.get_all()
