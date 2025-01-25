from pydantic import Field
from pydantic_settings import BaseSettings

class DbSettings(BaseSettings):
    DB_NAME: str = Field(env="DB_NAME")
    DB_USER: str = Field(env="DB_USER")
    DB_PASS: str = Field(env="DB_PASS")
    DB_HOST: str = Field(env="DB_HOST")
    DB_PORT: int = Field(env="DB_PORT")

class Settings(BaseSettings):
    secret_key: str = Field(env="SECRET_KEY")
    db: BaseSettings = DbSettings()

settings = Settings()