from fastapi import APIRouter, status, HTTPException
from functools import wraps

from .service import add_category, return_category, change_category, drop_category, add_product
from .schemas import ProductCreate, ProductReturn, CategoryCreate, CategoryReturn, SizeCreate, SizeReturn, AdditionalImageCreate, AdditionalImageReturn 

goods = APIRouter(prefix="/goods", tags=["goods"])

def check_result(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        if not result:
            raise HTTPException(404, 'There is no object with this id')
        return result

    return wrapper

@goods.get("/get_category/{category_id}", response_model=CategoryReturn)
@check_result
async def get_category(category_id: int):
    result = await return_category(category_id)
    return result

@goods.post("/create_category", response_model=CategoryReturn, status_code=status.HTTP_201_CREATED)
async def create_category(category_data: CategoryCreate):
    result = await add_category(category_data)
    return result

@goods.put("/update_category/category_id", response_model=CategoryReturn)
@check_result
async def update_category(category_id: int, category_data: CategoryCreate):
    result = await change_category(category_id, category_data)
    return result

@goods.delete("/delete_category")
@check_result
async def delete_category(category_id: int):
    result = await drop_category(category_id)
    if result:
        return HTTPException(200, "Successfully deleted")

# @goods.get("/get_product/{product_id}", response_model=ProductReturn)
# @check_result
# async def get_product(product_id: int):
#     result = await

@goods.post("/create_product", response_model=ProductCreate)
async def create_product(product_data: ProductCreate):
    result = await add_product(product_data)
    print(result)
    return result
