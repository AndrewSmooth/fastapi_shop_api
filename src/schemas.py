from pydantic import BaseModel


class AdditionalImageCreate(BaseModel):
    product: str
    path: str

class AdditionalImage(AdditionalImageCreate):
    id: int
    product_fk: int

class SizeCreate(BaseModel):
    name: str

class Size(SizeCreate):
    id: int

class CategoryCreate(BaseModel):
    name: str

class CategoryDTO(CategoryCreate):
    id : int

class ProductCreate(BaseModel):
    name: str 
    price: float
    category: str # Fk
    size_list: list # Fk
    description: str
    image: str # Fk (1 main image and 3 additional)
    ads: str #Fk additional images
    rating: float

class Product(ProductCreate):
    id: int
    slug: str # google it

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



