from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Env(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    CODZEN_TOKEN: str
    MODEL: str
    API_BASE_URL: AnyHttpUrl


env = Env()  # type: ignore[call-arg]
