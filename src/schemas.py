from pydantic import BaseModel

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



