from schemas.goods import SizeCreate 
from repositories.base_repository import AbstractRepository


class SizeService:
    def __init__(self, size_repo: AbstractRepository):
        self.size_repo: AbstractRepository = size_repo()

    async def add_size(self, data: SizeCreate):
        data_dict = data.model_dump()
        size_id = await self.size_repo.add_one(data_dict)
        return size_id

    async def edit_size(self, id: int, data: SizeCreate):
        data_dict = data.model_dump()
        size_id = await self.size_repo.edit_one(id, data_dict)
        return size_id
    
    async def delete_size(self, id: int):
        size_id = await self.size_repo.delete_one(id)
        return size_id
    
    async def get_size(self, id: int):
        size = await self.size_repo.get_one(id)
        return size

    async def get_sizes(self):
        sizes = await self.size_repo.get_all()
        return sizes