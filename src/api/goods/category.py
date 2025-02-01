from fastapi import APIRouter, status, HTTPException, Path

# from services.goods.category import add_category, return_category, change_category, drop_category, add_product
from schemas.goods import CategoryCreate, CategoryReturn
from ..dependencies import category_service, check_result

router = APIRouter(prefix="/category", tags=["Category"])


@router.post("", response_model=CategoryReturn)
@check_result
async def add_category(data: CategoryCreate): #Resp model
    result = await category_service().add_category(data)
    return result

@router.put("/{category_id}", response_model=CategoryReturn)
@check_result
async def edit_category(category_id: int, data: CategoryCreate): 
    result = await category_service().edit_category(category_id, data)
    return result

@router.delete("/{category_id}")
@check_result
async def delete_category(category_id: int): 
    result = await category_service().delete_category(category_id)
    return result

@router.get("/{category_id}", response_model=CategoryReturn)
@check_result
async def get_category(category_id: int = Path()): 
    result = await category_service().get_category(category_id)
    return result

@router.get("")
@check_result
async def get_categories():
    result = await category_service().get_categorires()
    return result