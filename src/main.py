from fastapi import FastAPI, Response, Cookie, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from datetime import datetime, timezone, timedelta
from contextlib import asynccontextmanager
import jwt

from database import database, get_session
from config import settings
from schemas import CategoryCreate, CategoryDTO
from models import Category


@asynccontextmanager
async def lifespan(application: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/")
async def root(session_token = Cookie(default=None)):
    return {"session_token": session_token}

@app.post("/create_category", response_model=CategoryDTO, status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryCreate):
    new_category = Category(name=category.name)
    session = get_session()
    session.add(new_category)
    await session.commit()
    await session.close()

    return CategoryDTO.model_validate(new_category, from_attributes=True)
