from pydantic import BaseModel, Field


class AdsCreate(BaseModel):
    product_fk: int = Field(alias="product_id")
    path: str

class AdsReturn(AdsCreate):
    id: int
    
class SizeCreate(BaseModel):
    name: str

class SizeReturn(SizeCreate):
    id: int

class CategoryCreate(BaseModel):
    name: str

class CategoryReturn(CategoryCreate):
    id : int

class ProductCreate(BaseModel):
    image: str
    name: str
    description: str
    price: float
    rating: float
    amount: int
    category_fk: int = Field(alias="category_id")
    size_fk: int = Field(alias="size_id")
    
class ProductReturn(ProductCreate):
    id: int

    class ConfigDict:
        populate_by_name=True