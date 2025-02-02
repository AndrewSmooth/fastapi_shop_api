from fastapi import FastAPI, Response, Cookie, Depends, status, HTTPException, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 

from pydantic import BaseModel

import pathlib
import aiofiles

from typing import Annotated
from contextlib import asynccontextmanager

import src.core.config as config
from src.core.database import database, Base, engine
# from tests.conftest import database
from src.api.routers import all_routers

import os

print("MODE:", os.getenv("MODE"))

absolute_path = pathlib.Path(__file__)
root_path = pathlib.PurePath(absolute_path).parents[1]


@asynccontextmanager
async def lifespan(application: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan, title="Shop")

for router in all_routers:
    app.include_router(router)
app.mount("/static", StaticFiles(directory="/media/andrew/DATA/FastAPI-Shop-Study/static"), name="static")


@app.get("/")
async def root(session_token = Cookie(default=None)):
    return {"session_token": session_token}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # Сделать проверку есть ли такое имя в бд и если есть, менять
    upload_path = root_path.joinpath("static", "uploads", file.filename)
    
    print("this", upload_path)
    async with aiofiles.open(upload_path, 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write
    return {"file": file.file}

@app.get("/sum/")
def calculate_sum(a: int, b: int):
    return {"result": a + b}


# class CustomExceptionModel(BaseModel):
#     status_code: int 
#     er_message: str 
#     er_details: str

# class ItemsResponse(BaseModel):
#     item_id: int

# class CustomException(HTTPException):
#     def __init__(self, detail: str, status_code: int, message: str):
#         super().__init__(status_code=status_code, detail=detail)
#         self.message = message

# @app.exception_handler(CustomException)
# async def custom_exception_handler(request: Request, exc: CustomException) -> JSONResponse:
#     error = jsonable_encoder(CustomExceptionModel(status_code=exc.status_code, er_message=exc.message, er_details=exc.detail))
#     return JSONResponse(status_code=exc.status_code, content=error)

# @app.exception_handler(Exception)
# async def global_exception_handler(request: Request, exc: Exception):
#     return JSONResponse(
#         status_code=500,
#         content={"error": "Internal server error"}
#     )


# @app.get("/items/{item_id}/", response_model=ItemsResponse)
# async def read_item(item_id: int):
#     # result = 1/0
#     try:
#         if item_id == 42:
#             raise ValueError("Cannt be 42")
#         # raise CustomException(detail="Item not found", status_code=404)
#     except ValueError as ve:
#         raise HTTPException(status_code=400, detail=str(ve))
#     return ItemsResponse(item_id=item_id)

# if __name__ == "__main__":
#     uvicorn.run(app="main:app", reload=True)


