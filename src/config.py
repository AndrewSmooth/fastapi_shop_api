from pydantic import BaseSettings, Field, BaseModel


class DbSettings(BaseSettings):
    pass
    # db_url: str = Field(enc="db_url")

class Settings(BaseSettings):
    secret_key: str = Field(env="SECRET_KEY")
    # db = DbSettings()

settings = Settings()