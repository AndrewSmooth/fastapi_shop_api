from fastapi import APIRouter, status, HTTPException

from schemas.goods import ProductCreate, ProductReturn
from ..dependencies import product_service, check_result

router = APIRouter(prefix="/product", tags=["Product"])

@router.post("", response_model=ProductReturn)
@check_result
async def add_product(data: ProductCreate):
    result = await product_service().add_product(data)
    return result

@router.put("/{product_id}", response_model=ProductReturn) 
@check_result
async def edit_product(product_id: int, data: ProductCreate): 
    result = await product_service().edit_product(product_id, data)
    return result

@router.delete("/{product_id}")
@check_result
async def delete_product(product_id: int): 
    result = await product_service().delete_product(product_id)
    return result

@router.get("/{product_id}", response_model=ProductReturn)
@check_result
async def get_product(product_id: int): 
    result = await product_service().get_product(product_id)
    return result

@router.get("")
@check_result
async def get_products():
    result = await product_service().get_products()
    print("LOG API")
    print(result)
    return result
