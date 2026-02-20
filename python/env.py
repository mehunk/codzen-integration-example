from pydantic_settings import BaseSettings, SettingsConfigDict


class Env(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    CODZEN_TOKEN: str


env = Env()  # type: ignore[call-arg]
