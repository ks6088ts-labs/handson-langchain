from pydantic import BaseSettings


class ChromaSettings(BaseSettings):
    openai_model_name = "text-embedding-ada-002"
    openai_deployment_id = "embedding"
    openai_api_type = "azure"
    openai_api_key = "YOUR_API_KEY"
    openai_api_base = "https://AOAI_NAME.openai.azure.com/"
    openai_api_version = "2023-07-01-preview"
    persist_directory = "data"
    collection_name = "chroma"

    class Config:
        env_file = "chroma.env"
