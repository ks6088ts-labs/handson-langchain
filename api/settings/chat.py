from pydantic import BaseSettings


class ChatSettings(BaseSettings):
    openai_model_name = "gpt-35-turbo"
    openai_deployment_id = "chat"
    openai_api_type = "azure"
    openai_api_key = "YOUR_API_KEY"
    openai_api_base = "https://AOAI_NAME.openai.azure.com/"
    openai_api_version = "2023-07-01-preview"

    class Config:
        env_file = "chat.env"
