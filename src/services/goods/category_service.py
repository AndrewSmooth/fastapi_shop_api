from schemas.goods import CategoryCreate
from repositories.base_repository import AbstractRepository


class CategoryService:
    def __init__(self, category_repo: AbstractRepository):
        self.category_repo: AbstractRepository = category_repo()

    async def add_category(self, data: CategoryCreate):
        data_dict = data.model_dump()
        category_id = await self.category_repo.add_one(data_dict)
        return category_id

    async def edit_category(self, id: int, data: CategoryCreate):
        data_dict = data.model_dump()
        category_id = await self.category_repo.edit_one(id, data_dict)
        return category_id
    
    async def delete_category(self, id: int):
        category_id = await self.category_repo.delete_one(id)
        return category_id
    
    async def get_category(self, id: int):
        category = await self.category_repo.get_one(id)
        return category

    async def get_categorires(self):
        categories = await self.category_repo.get_all()
        return categories
    






# from sqlalchemy import update, delete

# from ...models.goods import Product, Category
# from ...schemas.schemas import ProductCreate, ProductReturn, CategoryCreate, CategoryReturn, SizeCreate, SizeReturn, AdditionalImageCreate, AdditionalImageReturn 

# from core.database import get_session

# async def add_category(category: CategoryCreate):
#     new_category = Category(name=category.name)
#     session = get_session()
#     session.add(new_category)
#     await session.commit()
#     await session.close()
#     return CategoryReturn.model_validate(new_category, from_attributes=True)

# async def return_category(category_id: int):
#     session = get_session()
#     result = await session.get(Category, category_id)
#     await session.close()
#     print(result)
#     if not result:
#         return None
#     return CategoryReturn.model_validate(result, from_attributes=True)

# async def change_category(category_id: int, category: CategoryCreate):
#     session = get_session()
#     await session.execute(update(Category).where(Category.id==category_id).values(name=category.name))
#     await session.commit()
#     result = await session.get(Category, category_id)
#     await session.close()
#     return CategoryReturn.model_validate(result, from_attributes=True)

# async def drop_category(category_id: int):
#     session = get_session()
#     result = await session.execute(delete(Category).where(Category.id==category_id))
#     await session.commit()
#     await session.close()
#     return result

# async def add_product(product: ProductCreate):
#     session = get_session()
#     category = session.get(Category, product.category_id)
#     if not category:
#         print("invalid category id")
#         return {"Error": "Invalid Category"}
#     if category:
#         new_product = Product(
#             name=product.name,
#             description=product.description,
#             price=product.price,
#             rating=product.rating,
#             amount=product.amount,
#             category_id=product.category_id,
#             image=product.image,
#             )
#         session.add(new_product) 
#         await session.commit()
#         await session.close()
#         return ProductReturn.model_validate(new_product, from_attributes=True)