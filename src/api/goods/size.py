from fastapi import APIRouter, status, HTTPException

from schemas.goods import SizeCreate, SizeReturn
from ..dependencies import size_service, check_result

router = APIRouter(prefix="/size", tags=["Size"])

@router.post("", response_model=SizeReturn)
@check_result
async def add_size(data: SizeCreate):
    result = await size_service().add_size(data)
    return result

@router.put("/{size_id}", response_model=SizeReturn) 
@check_result
async def edit_size(size_id: int, data: SizeCreate): 
    result = await size_service().edit_size(size_id, data)
    return result

@router.delete("/{size_id}")
@check_result
async def delete_psize(size_id: int): 
    result = await size_service().delete_size(size_id)
    return result

@router.get("/{size_id}", response_model=SizeReturn)
@check_result
async def get_size(size_id: int): 
    result = await size_service().get_size(size_id)
    return result

@router.get("")
@check_result
async def get_sizes():
    result = await size_service().get_sizes()
    return result
