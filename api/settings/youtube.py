from pydantic import BaseSettings


class YouTubeSettings(BaseSettings):
    openai_model_name = "gpt-35-turbo-16k"
    openai_deployment_id = "gpt-35-turbo-16k"
    openai_api_type = "azure"
    openai_api_key = "YOUR_API_KEY"
    openai_api_base = "https://AOAI_NAME.openai.azure.com/"
    openai_api_version = "2023-12-01-preview"

    class Config:
        env_file = "youtube.env"
