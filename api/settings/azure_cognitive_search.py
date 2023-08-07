from pydantic import BaseSettings


class AzureCognitiveSearchSettings(BaseSettings):
    service_name = "YOUR_SERVICE_NAME"
    index_name = "YOUR_INDEX_NAME"
    api_key = "YOUR_API_KEY"

    class Config:
        env_file = "azure_cognitive_search.env"
