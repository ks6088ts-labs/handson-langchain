from pydantic import BaseSettings


class InformationSettings(BaseSettings):
    version: str = "0.0.0"
    revision: str = "fffffff"

    class Config:
        env_file = "information.env"
