from schemas.goods import ProductCreate
from repositories.base_repository import AbstractRepository


class ProductService:
    def __init__(self, product_repo: AbstractRepository):
        self.product_repo: AbstractRepository = product_repo()

    async def add_product(self, data: ProductCreate):
        data_dict = data.model_dump()
        print("LOG")
        print(data_dict)
        # data_dict["category_fk"]=data_dict.pop("category_id")
        # data_dict["size_fk"]=data_dict.pop("size_id")
        # print(data_dict)
        product = await self.product_repo.add_one(data_dict)
        print("LOG PRODUCT")
        print(product)
        # print(product.category_fk)
        # print(product)
        return product.to_read_model()

    async def edit_product(self, id: int, data: ProductCreate):
        data_dict = data.model_dump()
        product = await self.product_repo.edit_one(id, data_dict)
        # print(product.to_read_model())
        return product.to_read_model()
    
    async def delete_product(self, id: int):
        product = await self.product_repo.delete_one(id)
        return product
    
    async def get_product(self, id: int):
        product = await self.product_repo.get_one(id)
        return product.to_read_model()

    async def get_products(self):
        products = await self.product_repo.get_all()
        print("LOG")
        print(products)
        return products