from src.schemas.goods import AdsCreate
from src.repositories.base_repository import AbstractRepository


class AdsService:
    def __init__(self, ads_repo: AbstractRepository):
        self.ads_repo: AbstractRepository = ads_repo()

    async def add_ad(self, data: AdsCreate):
        data_dict = data.model_dump()
        print("LOG")
        print(data_dict)
        ad_id = await self.ads_repo.add_one(data_dict)
        print("LOG")
        print(data_dict)
        return ad_id.to_read_model()

    async def edit_ad(self, id: int, data: AdsCreate):
        data_dict = data.model_dump()
        ad_id = await self.ads_repo.edit_one(id, data_dict)
        return ad_id.to_read_model()
    
    async def delete_ad(self, id: int):
        ad_id = await self.ads_repo.delete_one(id)
        return ad_id
    
    async def get_ad(self, id: int):
        ad = await self.ads_repo.get_one(id)
        return ad.to_read_model()

    async def get_ads(self):
        ads = await self.ads_repo.get_all()
        return ads