from fastapi import APIRouter, status, HTTPException

from schemas.goods import AdsCreate, AdsReturn
from ..dependencies import ads_service, check_result

router = APIRouter(prefix="/ads", tags=["Additional Images"])

@router.post("", response_model=AdsReturn)
@check_result
async def add_ad(data: AdsCreate):
    result = await ads_service().add_ad(data)
    return result

@router.put("/{ad_id}", response_model=AdsReturn) 
@check_result
async def edit_ad(ad_id: int, data: AdsCreate): 
    result = await ads_service().edit_ad(ad_id, data)
    return result

@router.delete("/{ad_id}")
@check_result
async def delete_pad(ad_id: int): 
    result = await ads_service().delete_ad(ad_id)
    return result

@router.get("/{ad_id}", response_model=AdsReturn)
@check_result
async def get_ad(ad_id: int): 
    result = await ads_service().get_ad(ad_id)
    return result

@router.get("")
@check_result
async def get_ads():
    result = await ads_service().get_ads()
    return result
