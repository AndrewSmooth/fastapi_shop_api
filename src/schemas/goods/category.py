from pydantic import BaseModel


class AdditionalImageCreate(BaseModel):
    product: str
    path: str

class AdditionalImageReturn(AdditionalImageCreate):
    id: int
    product_fk: int

class SizeCreate(BaseModel):
    name: str

class SizeReturn(SizeCreate):
    id: int

class CategoryCreate(BaseModel):
    name: str

class CategoryReturn(CategoryCreate):
    id : int

class ProductCreate(BaseModel):
    name: str 
    price: float
    category_id: int # Fk
    # size_list: str # Fk
    description: str
    image: str # Fk (1 main image and 3 additional)
    # ads: str #Fk additional images
    rating: float
    amount: int

class ProductReturn(ProductCreate):
    id: int
    # slug: str # google it

class User(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    email: str

class UserReturn(BaseModel):
    username: str
    email: str
    id: int | None = None



