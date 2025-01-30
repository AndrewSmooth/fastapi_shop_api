from fastapi import APIRouter, status, HTTPException

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
async def get_category(category_id: int): 
    result = await category_service().get_category(category_id)
    return result

@router.get("")
@check_result
async def get_categories():
    result = await category_service().get_categorires()
    return result

# @goods.get("/get_category/{category_id}", response_model=CategoryReturn)
# @check_result
# async def get_category(category_id: int):
#     result = await return_category(category_id)
#     return result

# @goods.post("/create_category", response_model=CategoryReturn, status_code=status.HTTP_201_CREATED)
# async def create_category(category_data: CategoryCreate):
#     result = await add_category(category_data)
#     return result

# @goods.put("/update_category/category_id", response_model=CategoryReturn)
# @check_result
# async def update_category(category_id: int, category_data: CategoryCreate):
#     result = await change_category(category_id, category_data)
#     return result

# @goods.delete("/delete_category")
# @check_result
# async def delete_category(category_id: int):
#     result = await drop_category(category_id)
#     if result:
#         return HTTPException(200, "Successfully deleted")
    






    

# @goods.get("/get_product/{product_id}", response_model=ProductReturn)
# @check_result
# async def get_product(product_id: int):
#     result = await

# @goods.post("/create_product", response_model=ProductCreate)
# async def create_product(product_data: ProductCreate):
#     result = await add_product(product_data)
#     print(result)
#     return result
