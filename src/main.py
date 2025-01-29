from fastapi import FastAPI, Response, Cookie, Depends, status, HTTPException, File, UploadFile
from fastapi.staticfiles import StaticFiles

import pathlib
import aiofiles
from typing import Annotated
from contextlib import asynccontextmanager

from database import database
from goods.router import goods

absolute_path = pathlib.Path(__file__)
root_path = pathlib.PurePath(absolute_path).parents[1]

@asynccontextmanager
async def lifespan(application: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(goods)
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
