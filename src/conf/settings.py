from pydantic_settings import BaseSettings
from pydantic import Extra


class Settings(BaseSettings):
    app_title: str
    app_version: str
    app_description: str
    secret_key: str
    token_crypt_algorithm: str
    token_exp_time_min: int
    db_url: str

    class Config:
        env_file = None
        env_file_encoding = "utf-8"
        env_prefix = 'BK_'
        extra = Extra.allow


settings = Settings()
