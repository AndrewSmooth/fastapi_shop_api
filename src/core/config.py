from pydantic_settings import BaseSettings    
import os
from dotenv import load_dotenv

class Settings(BaseSettings):
    DB_NAME: str 
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    MODE: str
    DATABASE_URL: str
    # SECRET_KEY: str

# settings = Settings(env_file=os.getenv("ENV", ".env"))
load_dotenv(os.getenv("ENV", ".env"), override=True)
settings = Settings()
print(os.getenv("ENV"), settings.DB_NAME)