from pydantic_settings import BaseSettings, SettingsConfigDict


class InformationSettings(BaseSettings):
    version: str = "0.0.0"
    revision: str = "fffffff"

    model_config = SettingsConfigDict(env_file="information.env")
