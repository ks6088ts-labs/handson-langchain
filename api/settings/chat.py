from pydantic import BaseSettings


class ChatSettings(BaseSettings):
    openai_model_name: str = "gpt-35-turbo"
    openai_deployment_id: str = "chat"
    openai_api_type: str = "azure"
    openai_api_key: str = "YOUR_API_KEY"
    openai_api_base: str = "https://AOAI_NAME.openai.azure.com/"
    openai_api_version: str = "2023-07-01-preview"

    class Config:
        env_file = "chat.env"
