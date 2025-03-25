from fastapi import HTTPException
from functools import wraps

from src.repositories.goods_repository import CategoryRepository, ProductRepository, SizeRepository, AdsRepository
from src.services.goods.product_service import ProductService
from src.services.goods.category_service import CategoryService
from src.services.goods.size_service import SizeService 
from src.services.goods.ads_service import AdsService

def check_result(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        if not result:
            raise HTTPException(404, 'There is no object with this id')
        return result
    return wrapper

def category_service():
    return CategoryService(CategoryRepository)

def product_service():
    return ProductService(ProductRepository)

def size_service():
    return SizeService(SizeRepository)

def ads_service():
    return AdsService(AdsRepository)