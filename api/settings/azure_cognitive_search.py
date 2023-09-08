from pydantic import BaseSettings


class AzureCognitiveSearchSettings(BaseSettings):
    # Azure OpenAI Service for embedding
    openai_model_name = "text-embedding-ada-002"
    openai_deployment_id = "embedding"
    openai_api_type = "azure"
    openai_api_key = "YOUR_API_KEY"
    openai_api_base = "https://AOAI_NAME.openai.azure.com/"
    openai_api_version = "2023-07-01-preview"
    # Azure Cognitive Search
    azure_cognitive_search_endpoint = "https://COGSEARCH_NAME.search.windows.net"
    azure_cognitive_search_key = "YOUR_API_KEY"
    azure_cognitive_search_index_name = "YOUR_INDEX_NAME"

    class Config:
        env_file = "azure_cognitive_search.env"
