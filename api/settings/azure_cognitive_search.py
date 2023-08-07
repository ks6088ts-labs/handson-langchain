from pydantic import BaseSettings


class AzureCognitiveSearchSettings(BaseSettings):
    service_name: str
    index_name: str
    api_key: str

    class Config:
        env_file = "azure_cognitive_search.env"
