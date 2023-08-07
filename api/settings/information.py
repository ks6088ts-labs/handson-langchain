from pydantic import BaseSettings


class InformationSettings(BaseSettings):
    version = "0.0.0"
    revision = "fffffff"

    class Config:
        env_file = "information.env"
