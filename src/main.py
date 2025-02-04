from fastapi import FastAPI, Cookie, UploadFile, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

import pathlib
import aiofiles
import os

from contextlib import asynccontextmanager

import src.core.config as config
from src.core.database import database, Base, engine
from src.api.routers import all_routers
from src.utils.utils import get_upload_path


@asynccontextmanager
async def lifespan(application: FastAPI):
    await database.connect()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    if config.settings.MODE=="TEST":
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    await database.disconnect()


app = FastAPI(lifespan=lifespan, title="Shop")
app.mount("/static", StaticFiles(directory="/media/andrew/DATA/FastAPI-Shop-Study/static"), name="static")
for router in all_routers:
    app.include_router(router)

absolute_path = pathlib.Path(__file__)
root_path = pathlib.PurePath(absolute_path).parents[1]

print("MODE:", os.getenv("MODE"))


@app.middleware("http")
async def filter_static(request: Request, call_next):
    if request.url.path.startswith("/static") and \
        (not request.url.path.endswith(".jpg") or not request.url.path.endswith(".png")):
        return JSONResponse({"error":"Cannot find the file specified"}, status_code=404)
    response = await call_next(request)
    return response

@app.get("/")
async def root(session_token = Cookie(default=None)):
    return {"session_token": session_token}

@app.post("/uploadimage/")
async def create_upload_file(file: UploadFile):
    new_filename = file.filename.lower().replace(" ", "_")
    print(new_filename)
    upload_path = root_path.joinpath("static", "uploads", new_filename)   
    upload_path = get_upload_path(str(upload_path))
    async with aiofiles.open(upload_path, 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write
    return {"path": upload_path}

  